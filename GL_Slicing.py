import cv2
import numpy as np

def graylevelslicing(img, beginning, finish, result):
    row = img.shape[0]
    column = img.shape[1]

    new_img = np.zeros((row, column), dtype='uint8')

    for i in range(row):
        for j in range(column):
            if img[i,j]>beginning and img[i,j]<finish:
                new_img[i,j] = result
            else:
                new_img[i,j] = img[i,j]

    cv2.imshow("graylevelsliced", new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()