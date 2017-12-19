import sys
import os
import time
import requests
import redis

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
redis_db = redis.StrictRedis(host="24.24.24.134", port=6379)

class SystemToolTime(Resource):
    def get(self):
        ##url = "http://" + os.environ['APP'] + "-system-time:10002/time"
        #url = "http://" + os.environ['APP'] + "-system-time"
        
        url = redis_db.get('SYSTEM-TIME-1513')
        headers = {            
            'API-KEY': redis_db.get('API-KEY')
            }
        resp = requests.request("GET", url, headers=headers)
        #resp = requests.get(url)
        return resp.json()


class SystemToolUpTime(Resource):
    def get(self):
        ##url = "http://" + os.environ['APP'] + "-system-uptime:10004/uptime"
        #url = "http://" + os.environ['APP'] + "-system-uptime"
        url = redis_db.get('SYSTEM-UPTIME-1512')
        headers = {            
            'API-KEY': redis_db.get('API-KEY')
            }
        resp = requests.request("GET", url, headers=headers)
        #resp = requests.get(url)
        return resp.json()


api.add_resource(SystemToolTime, '/systemtoolstime')
api.add_resource(SystemToolUpTime, '/systemtoolsuptime')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10000
    
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
