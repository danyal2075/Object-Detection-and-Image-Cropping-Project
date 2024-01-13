import cv2
import pandas as pd
from PIL import Image 
from crop import object_crop
from model import model_prediction
import time
import os
import shutil
import argparse


def unittest():
    pass

def prediction():
    pass

def test():
    '''
    When calling the test function without any image path as input. 
    It will show an image before crop and after crop and also show a detected object. 
    It means you will choose any image from testing data.
    '''
    # Delete previous prediction and croppped object.
    print('Test Function is called')

    for i in os.listdir("./runs/detect"):
        shutil.rmtree(f"./runs/detect/{i}")
    for i in os.listdir("./Cropped_images"):
        os.remove(f"./Cropped_images/{i}")


    # New Predictions    
    result = model_prediction(args.data_path)
    # result.show(), result.save()
    result.save(), result.show()

    # Creating DataFrame of the results. Use saved to crop the image
    df = result.pandas().xyxy[0]
    df.to_csv('results.csv', index = False)
    time.sleep(5)
    
    # Finding csv file.
    for f in os.listdir():
        if f.endswith('.csv'):
            info_path = f

    # use of csv file to get coordinates, width and height to crop the image
    object_crop(args.data_path, info_path)

    # Showing Cropped Object
    for i in os.listdir("./Cropped_images"):
        cv2.imshow(f"./Cropped_images/{i}", f"{i}")
        cv2.waitKey(0)
    print('Predictions Done')


def main(args):
    if args.test:
        test(args.showorginalsample, args.cropobject)
    else:
    # Delete previous prediction and croppped object.
        for i in os.listdir("./runs/detect"):
            shutil.rmtree(f"./runs/detect/{i}")
        for i in os.listdir("./Cropped_images"):
            os.remove(f"./Cropped_images/{i}")


        # New Predictions    
        result = model_prediction(args.data_path)
        # result.show(), result.save()
        result.save()
        if args.showorginalsample:
            result.show() 
        
        # Creating DataFrame of the results. Use saved to crop the image
        df = result.pandas().xyxy[0]
        df.to_csv('results.csv', index = False)
        time.sleep(5)
        
        # Finding csv file.
        for f in os.listdir():
            if f.endswith('.csv'):
                info_path = f

        # use of csv file to get coordinates, width and height to crop the image
        object_crop(args.data_path, info_path)
        print('Predictions Done')


def arg(help = True):
    parser = argparse.ArgumentParser(description= 'Object Detection and Cropping Project', add_help= help)
    parser.add_argument('--data-path', default=r".\test_data\dog.jpg", type= str, help= 'Pass the image path')
    parser.add_argument('--showorginalsample', default= False, type= bool, help= 'Make it true want to see orginal image' )
    parser.add_argument('--cropobject', default= False, type= bool, help='Make True to see cropped object')
    parser.add_argument('--test', default= False, type= bool, help= 'testing whole project')

    return parser.parse_args()

if __name__ == "__main__":

    args = arg()
    main(args)



