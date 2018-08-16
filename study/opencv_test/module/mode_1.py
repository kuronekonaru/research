import numpy as np
import cv2 as cv

# mode_1 function

def read_image():
    file_name = "img/Chrysanthemum.jpg"
    img = cv.imread(file_name,3)
    return img

def excute_mode_1():
    print("mode_1")
    cv.namedWindow('mode_1')
    cv.imshow('mode_1',read_image())
