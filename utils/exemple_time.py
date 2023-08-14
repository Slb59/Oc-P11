# import os
from datetime import datetime
import pytz
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/time')
def time():
    # Default sever level date and time
    current_server_time = datetime.now()
    if 'timezone' in request.args:
        tzinfo = pytz.timezone(request.args['timezone'])
        # Converting date and time based on timeone input from client
        current_client_time = current_server_time.astimezone(tzinfo)
        return jsonify({"time": current_client_time})
    return jsonify({"time": current_server_time})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
