import os
import cv2
import pandas as pd

for file in os.listdir('./test_data'):
    print(file)
    img = cv2.imread(file)
    cv2.imshow(f'{file}',file) 