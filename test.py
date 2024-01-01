import os
import cv2
import pandas as pd


def display_results(path = None):
    

    if path:
        # print(os.path.split(path)[1])
        for f in os.listdir():
            if f.endswith('.csv'):
                info_path = f
        df = pd.read_csv(info_path)
        print(df.iloc[:,4:])

        print("Orginial Image")
        test_img = cv2.imread(path)
        cv2.imshow(f'{os.path.split(path)[1]}',test_img)
        cv2.waitKey(0)

        img_paths = [] 
        i_path = []
        for r_file in os.listdir('./Cropped_images'):
            r_path = os.path.join('./Cropped_images/', r_file)
            img_paths.append(r_path)
            i_path.append(r_file)

        print("Cropped Images")
        for idx, result_img in enumerate(img_paths):
            result_imgs = cv2.imread(result_img)
            cv2.imshow(f'{i_path[idx]}',result_imgs)
            cv2.waitKey(0)

        cv2.waitKey() == 13
        cv2.destroyAllWindows()
    else:
        f_path = [os.path.join('./test_data/', file) for file in os.listdir('./test_data')]

        img_paths = [] 
        i_path = []
        for r_file in os.listdir('./Cropped_images'):
            r_path = os.path.join('./Cropped_images/', r_file)
            img_paths.append(r_path)
            i_path.append(r_file)

        print("Orginial Image")
        test_img = cv2.imread(f_path[0])
        cv2.imshow('Orginal Sample',test_img)
        cv2.waitKey(0)


        print("Cropped Images")
        for idx, result_img in enumerate(img_paths):
            result_imgs = cv2.imread(result_img)
            cv2.imshow(f'{i_path[idx]}',result_imgs)
            cv2.waitKey(0)

        cv2.waitKey() == 13
        cv2.destroyAllWindows()
display_results(path = './test_data/dog.jpg')

# import os
# import cv2

# def display_images(folder, prefix=''):
#     img_paths = [os.path.join(folder, file) for file in os.listdir(folder)]
#     for idx, img_path in enumerate(img_paths):
#         img = cv2.imread(img_path)
#         cv2.imshow(f'{prefix}_{idx}', img)
#         cv2.waitKey(1000)  # Adjust the delay between images (milliseconds)

# # Display original test image
# test_data_folder = './test_data'
# display_images(test_data_folder, prefix='original')

# # Display cropped result images
# cropped_images_folder = './Cropped_images'
# display_images(cropped_images_folder, prefix='cropped')

# cv2.waitKey() == 13
# cv2.destroyAllWindows()

