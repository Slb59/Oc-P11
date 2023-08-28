import webbrowser
import gevent
# import subprocess
import importlib, importlib.util

from multiprocessing import Process
from locust.env import Environment
from locust import events
from locust.stats import stats_printer, stats_history

# from gudlft.server import app
from locustfile import GudlftPerfTest


def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module


def start_flaskapp():
    gudlft_server = module_directory("gudlft", "gudlft/server.py")
    gudlft_server.app.run(debug=True)
    # subprocess.run('export FLASK_APP=server.py')
    # subprocess.run('flask run')


def start_8089_webui():
    webbrowser.open_new_tab('http://localhost:8089')


def start_locust():

    # setup Environment and Runner
    env = Environment(user_classes=[GudlftPerfTest], events=events)
    runner = env.create_local_runner()

    # start a WebUI instance
    web_ui = env.create_web_ui("localhost", 8089)

    # execute init event handlers (only really needed if you have registered any)
    env.events.init.fire(environment=env, runner=runner, web_ui=web_ui)

    # start a greenlet that periodically outputs the current stats
    gevent.spawn(stats_printer(env.stats))

    # start a greenlet that save current stats to history
    gevent.spawn(stats_history, env.runner)

    # start the test
    runner.start(6, spawn_rate=1)

    # in 60 seconds stop the runner
    gevent.spawn_later(60, lambda: runner.quit())

    # wait for the greenlets
    runner.greenlet.join()

    # stop the web server for good measures
    web_ui.stop()

    print('Rapport des tests de performance')
    print('--------------------------------')
    print(f'fail_ratio: {env.runner.stats.total.fail_ratio:.0f} %')
    print(f'avg_response_time: {env.runner.stats.total.avg_response_time:.0f} ms')


start_flaskapp()
start_8089_webui()
start_locust()
