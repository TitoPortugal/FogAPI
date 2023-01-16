#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:31:54 2023

@author: tito
"""

import torch

def yolo_inference():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    imgs = ['https://ultralytics.com/images/zidane.jpg']
    results = model(imgs)
    # results.print()
    # results.save()
    # print(results)
    return results.pandas().xyxy[0].to_json(orient="records")

