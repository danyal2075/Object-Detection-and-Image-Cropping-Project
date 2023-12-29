import cv2
import pandas as pd
from PIL import Image 
from crop import object_crop
from model import model_prediction
import time



def main(image_path,info_path):
    result = model_prediction(image_path)
    result.show(), result.save() 
    # Creating DataFrame of the results. Use saved to crop the image
    df = result.pandas().xyxy[0]
    df.to_csv('results.csv', index = False)
    time.sleep(5)
    object_crop(image_path, info_path)



if __name__ == "__main__":
    image_path = "dog.jpg"
    info_path = "results.csv"
    main(image_path,info_path)