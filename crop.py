import cv2
import pandas as pd

def object_crop(image_path, info_path):
    # Read the image
    
    image = cv2.imread(image_path)
    df = pd.read_csv(info_path)
    # Iterate over rows in the DataFrame
    for index, row in df.iterrows():
        xmin, ymin, xmax, ymax = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        class_name = row['name']

        # Crop the object from the image
        cropped_object = image[ymin:ymax, xmin:xmax]
        cv2.imshow(f"{class_name}",cropped_object)
        cv2.waitKey(0)
    
        # Save or process the cropped object as needed
        cv2.imwrite(f'Cropped_images/{class_name}_{index}.png', cropped_object)
    cv2.destroyAllWindows()