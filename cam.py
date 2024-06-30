import cv2 as cv

cam=cv.VideoCapture(0)
while cam.isOpened():
    success,img=cam.read()
    cv.imshow('img',img)
    if cv.waitKey(60)& 0xFF==ord('q'):
        break              