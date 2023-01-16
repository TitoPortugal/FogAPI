#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:36:33 2023

@author: tito
"""

import torch

import urllib
# from torchvision.models import resnet50, ResNet50_Weights
# from torchvision.models import resnet50

from PIL import Image
from torchvision import transforms

url,filename  = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg","./src/models/dog.jpg")

# try: urllib.URLopener().retrieve(url, filename)
# except: urllib.request.urlretrieve(url, filename)

def resnet_inference():
    model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet50', pretrained=True)
    # model = resnet50(weights='DEFAULT')
    model.eval()
    
    input_image = Image.open(filename)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.465, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')
    with torch.no_grad():
        output = model(input_batch)
    
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    return str(probabilities.tolist())
    
    