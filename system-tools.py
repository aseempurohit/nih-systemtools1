import sys
import os
import time
import requests

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class SystemToolTime(Resource):
    def get(self):
        ##url = "http://" + os.environ['APP'] + "-system-time:10002/time"
        url = "http://" + os.environ['APP'] + "-system-time"
        resp = requests.get(url)
        return resp.json()


class SystemToolUpTime(Resource):
    def get(self):
        ##url = "http://" + os.environ['APP'] + "-system-uptime:10004/uptime"
        url = "http://" + os.environ['APP'] + "-system-uptime"
        resp = requests.get(url)
        return resp.json()


api.add_resource(SystemToolTime, '/systemtoolstime')
api.add_resource(SystemToolUpTime, '/systemtoolsuptime')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10000
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
