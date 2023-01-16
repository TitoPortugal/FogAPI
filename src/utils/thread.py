#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:31:54 2023

@author: tito
"""
from threading import Thread

class Cthread(Thread):
    def __init__(self, target=None, name=None, args=(), kwargs={}, daemon=None):
        #super(Cthread,self).__init__(group=group,target=target,name=name,args=args,kwargs=kwargs,daemon=daemon)
        Thread.__init__(self)
        self.result = None
        self._target= target
        self.name= name
        self._args = args
        self._kwargs = kwargs
    
    def run(self):
        # print(self.result)
        self.result = self._target()
        # print(type(self.result))
        
        