# -*- coding: utf-8 -*-

import tornado.web
import threading
import json
import time
from tornado.httpclient import AsyncHTTPClient


class FogMaster:
    def __init__(self):
        self.app = self.make_app()
        self._lock = threading.Lock()
        

    class TaskHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Task handler")
        
        def post(self):
            # Receive a task
            self.write("Receiving task")
    
    class StatusHandler(tornado.web.RequestHandler):
        def get(self,status):
            self.write("Status handler, %s" %  status)
            
    def make_app(self):
        return tornado.web.Application([
            tornado.web.url(r"/task/", self.TaskHandler),
            tornado.web.url(r"/status/([01]?[0-9][0-9]?)", self.StatusHandler, None, name="status")
        ])
    
    async def request_status(self, file_name="fog_status.json", update_time=60):                
        with self._lock:
            with open(file_name) as f:
                data = json.load(f)
            output = data.copy()
            for node in data:
                url = "http://"+ node + ":8888/status"
                http = AsyncHTTPClient()
                response = await http.fetch(url)
                output[node] = response.body
                print(response.body)
            with open(file_name, "w") as output_file:
                output_file.write(json.dumps(output))
                        
    
    def main(self, configuration):
        
        while True:    
            statusthread = threading.Thread(target=self.request_status())
            statusthread.start()
            statusthread.join()
            time.sleep(60)
            