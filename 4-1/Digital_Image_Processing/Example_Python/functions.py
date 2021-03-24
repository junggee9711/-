import cv2
import numpy as np


def reverse(input_img, iHeight, iWidth):
    
    output_img = np.zeros((iHeight, iWidth, 1))
    output_img2 = np.zeros((iHeight, iWidth, 1))
    
    for iH in range(0, iHeight):
        for iW in range(0, iWidth):
            output_img[iH, iW, 0] = 255 - imput_img[iH, iW, 0]
            
    output_img2 = 255 - input_img    
           
    return output_img.astype(np.uint8), output_img2.astype(np.uint8)


def gradation(iHeight, iWidth):
   
    output_img = np.zeros((iHeight, iWidth, 1))
    output_img2 = np.zeros((iHeight, iWidth, 1))
    
    for iH in range(0, iHeight):
        for iW in range(0, iWidth):
            output_img[iH, iW, 0] = iH    
    for iH in range(0, iHeight):
        for iW in range(0, iWidth):
            output_img2[iH, iW, 0] = iW    
        
    return output_img.astype(np.uint8), output_img2.astype(np.uint8)