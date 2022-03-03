#Deformar
import cv2
import numpy as np

img =cv2.imread("Python\Advanced Computer Vision with Python\OpenCv Basico\Moc-apresentacao-6.png")


width,height = 800,800
pts1 = np.float32([[383,508],[1000,406],[500,895],[1136,739]]) #A imagem referencia foi aberta no paint e descoberta as coordenadas das borda do cartao
pts2 = np.float32([[0,0],[width,0],[0,width],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

#cv2.imshow("Image",img)
cv2.imshow("imgOutput",imgOutput)


cv2.waitKey(0)