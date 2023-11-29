import os
import cv2 
import torch 

def processImages(directory,preprocessor):
    images=[]

    for image_path in  os.listdir(directory):
        full_path=os.path.join(directory,image_path)
        image=cv2.imread(full_path)
        processed_image = preprocessor(image)
        images.append(processed_image)
    
    preprocessed_dataset= torch.stack(images)
    return preprocessed_dataset
