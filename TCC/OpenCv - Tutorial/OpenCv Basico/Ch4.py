#Formas e Texto
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)       #Zero = preto
#print(img)

#Preencer a janlea com um retangulo generico preenchido

#img[200:300,100:400] = 255,0,0 #Altura x Comprimento [inicio:fim]
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)  #Sem preenchimento
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #Com preenchimento

#Desenhar linha

#cv2.line(img,(0,0),(300,300),(250,200,5))                      #Linha entre dois pontos especificos
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(250,200,5),3)   #Diagonal e o ultimo valor é a espessura

#Desenhar Circulo
cv2.circle(img,(256,256),30,(255,255,0),5)

#Colocar Texto
cv2.putText(img,"OPEN_CV",(180,320),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2 )

cv2.imshow("Image",img)

cv2.waitKey(0)