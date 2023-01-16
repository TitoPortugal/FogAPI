#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:24:40 2022

@author: tito
"""


import asyncio

import tornado.web

import argparse
import yaml
from yaml.loader import SafeLoader

from src.mode.master import FogMaster
from src.mode.worker import FogWorker

def get_args():
    parser = argparse.ArgumentParser(
        description="")
    # parser.add_argument("source", type=str,
    #                     help="The path of the input source.")
    parser.add_argument("--master", default=False, action='store_true',
                        help="Choose between master mode or worker mode.")
    args = parser.parse_args()
    return args
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")



async def main(args):
    if args.master:
        app = FogMaster().app
    else:
        app = FogWorker().app
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":                
    args = get_args()
    
    with open('configuration.yaml','r') as f:
        conf = yaml.load(f, Loader=SafeLoader)
    
    if args.master:
        print(conf)

    asyncio.run(main(args))