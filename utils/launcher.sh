# simple shortcut that runs the flask app within its environment
pipenv shell
export FLASK_APP=gudlft/server.py
export FLASK_DEBUG=1
# export PYTHONPATH="projectpath"
flask run