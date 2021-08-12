import cv2
from GL_Slicing import graylevelslicing

inimg = cv2.imread("COINS.TIF",0)
cv2.imshow("Original",inimg)
graylevelslicing(inimg, 50, 150, 200)