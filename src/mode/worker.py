# -*- coding: utf-8 -*-

import tornado.web
import asyncio
import threading
from src.models.yolo import yolo_inference
from src.models.resnet import resnet_inference
from src.utils.thread import Cthread
from src.utils.status import Status


class FogWorker:
    def __init__(self):
        self.app = self.make_app()

    class TaskHandler(tornado.web.RequestHandler):
        # def get(self):
        #     self.write('<html><body><form action="/task" method="POST">'
        #                '<input type="text" name="message">'
        #                '<input type="submit" value="Submit">'
        #                '</form></body></html>')
        
       async def get(self, task_type, model):
            # Receive a task
            self.write("Receiving task" + task_type + model )
            # th = threading.Thread(target = yolo_inference, args=())
            # th.start()
            if task_type == 'detection':
                function = yolo_inference
            elif task_type == 'classification':
                function = resnet_inference
            thread = Cthread(target = function)
            thread.start()
            thread.join()
            self.write(thread.result)
    
    class StatusHandler(tornado.web.RequestHandler):
        def get(self):
            # self.write("Status handler, %s" %  status)
            status = Status()
            self.write(status.toJson())
    
    def make_app(self):
        return tornado.web.Application([
            tornado.web.url(r"/task/(detection|classification)/(yolo|resnet)", self.TaskHandler),
            tornado.web.url(r"/status", self.StatusHandler)
        ])
    async def main(self):
        self.app.listen(8888)
        await asyncio.Event().wait()
    


