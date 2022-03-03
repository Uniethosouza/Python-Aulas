#Re-size
import cv2
import numpy as np


img = cv2.imread("C:/Users/thoma/Desktop/Aprendizado/Corvo.png")
print(img.shape)        #(1084, 1480, 3) 1084 - Altura , 1480 - LArgura , Canal:VGR

imgResize = cv2.resize(img,(1920,1080))     #Resize - Largura x Comprimento
print(imgResize.shape)
#imgCropped = img[20:800,20:800]                      #Relaçao inversa - Altura primeiro e depois LArgura


cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgResize)

cv2.waitKey(0)