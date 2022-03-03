import cv2

#Ver imagens

#img = cv2.imread("C:/Users/thoma/Desktop/Aprendizado/ImagemGenerica.jpg")   #Seleciona a imagem
#cv2.imshow("Output",img)                                                    #Chama a imagem
#cv2.waitKey(5000)                                                              #Demostra a imagem Infinitamente - 0 = Infinito || 1000 = 1 segundo


#Ver Video

#cap = cv2.VideoCapture("C:/Users/thoma/Desktop/Aprendizado/Manim/media/videos/Exemplo1Manim/720p30/ComplexExp.mp4")
#while True:                                                                 #Para mostrar todos os frames do video
   # success, img2 = cap.read()
  #  cv2.imshow("Video",img2)
 #   if cv2.waitKey(1) & 0xff == ord('q'):                                   #Espera a tecla q para Parar de assistir o video
#        break

#Usando a WebCam

cap1 = cv2.VideoCapture(0)                                                    #WebCam começa em zero, mas o index pode aumenter se houver mais
cap1.set(3,640)                                                               #Largura  , 640 pixels
cap1.set(4,480)                                                               #Altura   , 480 pixels
cap1.set(10,100)                                                              #Brilho

while True:                                                                  #Para mostrar todos os frames do video
    success, img2 = cap1.read()
    cv2.imshow("Video",img2)
    if cv2.waitKey(1) & 0xff == ord('q'):                                     #Espera a tecla q para Parar de assistir o video
        break