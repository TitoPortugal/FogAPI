# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:34:45 2023

@author: titoo
"""

import gymnasium as gym
import numpy as np
import threading

from gymnasium import spaces
from src.mode.master import FogMaster

class FogEnv(gym.Env):
    
    def __init__(self, configuration = None):
        assert configuration, "Configuration parameter has to be a dictionary"
        self.master = FogMaster(configuration)
        
        #Action space
        self.action_space = spaces.Discrete(len(configuration["node_ips"]["workers"]))
        
        #Observation space
        self.observation_space = spaces.Dict({
                "status": spaces.Box(low=[0,0,0,0], high=[1, 1, 10000, 1000000], dtype=np.float32),
                "task": spaces.Discrete(100)
            })
    
    def step():
        return
    
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        #Initial observation
        statusthread = threading.Thread(target=self.master.request_status())
        statusthread.start()
        statusthread.join()
        observation = {
            
            }
        info = None
        return observation, info
    
