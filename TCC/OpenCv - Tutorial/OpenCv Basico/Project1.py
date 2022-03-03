
import cv2
import numpy as np

cap = cv2.VideoCapture(0)                                  
cap.set(3,640)                                                               
cap.set(4,480)                                                               
cap.set(10,100)             

mycolor = [[72,120,61,217,146,255],
            [34,146,80,207,99,251]]
mycolorValues = [[0,248,120],         #BGR != RGB
                 [0,115,0]] 
mypoint =  []#[x,y,colorID]

def findColor(img, mycolor,mycolorValues ): 
    count = 0
    newpoint=[]
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in mycolor:
        lower =np.array(color[0:3])
        upper =np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y =getContours(mask)       
        cv2.circle(imgResult,(x,y),10,mycolorValues[count],cv2.FILLED) 
        if x!=0 and y!=0:
            newpoint.append([x,y,count])
        count =+ 1
        #cv2.imshow(str(color[0]),mask)
    return newpoint 
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        areas = cv2.contourArea(cnt)
        if areas >400 :
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(mypoint,mycolorValues):
    for point in mypoint:
        cv2.circle(imgResult,(point[0],point[1]),10,mycolorValues[point[2]],cv2.FILLED) 
         
while True:                                                                 
    success, img = cap.read()
    imgResult = img.copy()
    newpoint = findColor(img,mycolor,mycolorValues)
    if len(newpoint)!=0 :
        for newp in newpoint:
            mypoint.append(newp)
    if len(mypoint)!=0 :
        drawOnCanvas(mypoint,mycolorValues)

    cv2.imshow("Video",imgResult)
    if cv2.waitKey(1) & 0xff == ord('q'):                                    
        break
