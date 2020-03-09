import cv2
import numpy as np
#red==1
lowerBound1=np.array([160,100,100])
upperBound1=np.array([179,255,255])
#green==2
lowerBound2=np.array([33,80,40])
upperBound2=np.array([90,255,255])
#blue==3
lowerBound3=np.array([100,86,40])
upperBound3=np.array([121,255,255])
#yellow==4
lowerBound4=np.array([20,100,100])
upperBound4=np.array([30,255,255])
#ORANGE==5
lowerBound5=np.array([10,100,100])
upperBound5=np.array([20,255,255])


def findshape(img):
    imgGRAY=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(imgGRAY, 100, 255)
    img2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    image = 0

    for cnt in contours:
        area=cv2.contourArea(cnt)
        hull = cv2.convexHull(cnt)
        approx = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
        if len(approx)==4:
            name="quadilateral"
        elif len(approx)==5:
            name="pentagon"
        elif len(approx)==3:
            name="Triangle"

        elif len(approx) > 7:
            name="circle"
        else:
            name="shape not detect"
        if(area>50):
            M=cv2.moments(cnt)
            Cx=( int(M['m10']/M['m00']) )
            Cy=( int(M['m01']/M['m00']) )
            cv2.putText(img, name, (Cx, Cy), cv2.FONT_HERSHEY_SIMPLEX,0.4, (255, 0, 0), 1)
def findcolor(color):
    if color==1:
        mask = cv2.inRange(imgHSV, lowerBound1,upperBound1)
        col = cv2.bitwise_and(img,img, mask= mask)
        #findshape(col)
        cv2.imshow("image",img)
        cv2.imshow("Red coloured Objects",col)
        #cv2.imwrite("redout.png",col)
    if color==2:
        mask = cv2.inRange(imgHSV, lowerBound2,upperBound2)
        col = cv2.bitwise_and(img,img, mask= mask)
        #findshape(col)
        cv2.imshow("image",img)
        cv2.imshow("Green coloured Objects",col)
        #cv2.imwrite("greenout.png",col)
    if color==3:
        mask = cv2.inRange(imgHSV, lowerBound3,upperBound3)
        col = cv2.bitwise_and(img,img, mask= mask)
        #findshape(col)
        cv2.imshow("image",img)
        cv2.imshow("Blue coloured Objects",col)
        #cv2.imwrite("blueout.png",col)
    if color==4:
        mask = cv2.inRange(imgHSV, lowerBound4,upperBound4)
        col = cv2.bitwise_and(img,img, mask= mask)
        #findshape(col)
        cv2.imshow("image",img)
        cv2.imshow("Yellow coloured Objects",col)
        #cv2.imwrite("yellowout.png",col)
    if color==5:
        mask = cv2.inRange(imgHSV, lowerBound5,upperBound5)
        col = cv2.bitwise_and(img,img, mask= mask)
        #findshape(col)
        cv2.imshow("image",img)
        cv2.imshow("Orange coloured Objects",col)
        #cv2.imwrite("orangeout.png",col)

cap = cv2.VideoCapture(1)
#img =cv2.imread("45.png")
while(1):
    _,img = cap.read()
    bluredimg=cv2.GaussianBlur(img,(5,5),1)
    imgGRAY=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    findcolor(1)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()