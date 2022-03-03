import cv2
import numpy as np

img = cv2.imread("ImagemGenerica2.png")
kernel =np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      # Converter para Cinza
imgBlur = cv2.GaussianBlur(imgGray ,(7,7),0)        # Ofuscar
imgCanny = cv2.Canny(img,100,100)                   # Um operador de detecção de bordas que usa um algoritmo de vários 
                                                    #estágios para detectar uma ampla gama de bordas nas imagens
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


#cv2.imshow("Gray Image", imgGray)
#cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Corrod Image", imgEroded)

cv2,cv2.waitKey(0)