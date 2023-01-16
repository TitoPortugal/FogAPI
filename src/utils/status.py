#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:52:12 2023

@author: tito
"""

import psutil
import GPUtil
import json

class Status:
    def __init__(self):
        self.total_cores = psutil.cpu_count(logical=True)
        self.physical_cores = psutil.cpu_count(logical=False)
        self.total_cpu_usage = psutil.cpu_percent()
        self.percent_memory_usage = psutil.virtual_memory().percent
        try:
            self.gpus = GPUtil.getGPUs()
        except:
            self.gpus = None
    
    def toURL(self):
        output = f"{self.total_cpu_usage}/{self.percent_memory_usage}"
        if self.gpus:
            for gpu in self.gpus:
                memory_used = (gpu.memoryUsed / gpu.memoryTotal) * 100
                output += f"/gpu-{gpu.id}-{gpu.load}-{memory_used:.2f}"
        else:
            output += "/nogpu"
        return output
    
    def toJson(self):
        output = {"cpu_usage": self.total_cpu_usage,
                  "memory_usage": self.percent_memory_usage}
        if self.gpus:
            output["gpus"] = self.gpus
        return output
            
        
        
        