import numpy as np
import pandas as pd
import os
import cv2 #useful to read and iterate through images
import torch
import torchvision.transforms as transforms

class CelebAPreprocessing(transforms.Compose):
    def __init__(self):
        super().__init__()
        self.transforms = [
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
            transforms.Grayscale(num_output_channels=1)
        ]
