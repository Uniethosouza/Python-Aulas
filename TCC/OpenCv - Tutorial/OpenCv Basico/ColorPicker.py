#Colour detection
import cv2
import numpy as np

cap = cv2.VideoCapture(0)                                                    #WebCam começa em zero, mas o index pode aumenter se houver mais
cap.set(3,640)                                                               #Largura  , 640 pixels
cap.set(4,480)                                                               #Altura   , 480 pixels
cap.set(10,100)                                                              #Brilho


def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)

cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    _, img = cap.read()

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min  = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max  = cv2.getTrackbarPos("Hue Max","TrackBars")
    Sat_min= cv2.getTrackbarPos("Sat Min","TrackBars")
    Sat_max= cv2.getTrackbarPos("Sat Max","TrackBars")
    Val_Min= cv2.getTrackbarPos("Val Min","TrackBars")
    Val_Max= cv2.getTrackbarPos("Val Max","TrackBars")

    print(h_min,h_max,Sat_min,Sat_max,Val_Min,Val_Max)

    lower =np.array([h_min,Sat_min,Val_Min])
    upper =np.array([h_max,Sat_max,Val_Max])
    mask = cv2.inRange(imgHSV,lower,upper)
    
    result = cv2.bitwise_and(img,img,mask=mask)

   
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])

    cv2.imshow("Video",hstack)
    if cv2.waitKey(1) & 0xff == ord('q'):                                     #Espera a tecla q para Parar de assistir o video
        break

cap.release()
cv2.destroyAllWindows()