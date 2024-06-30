import cv2 as cv

capture=cv.VideoCapture('Videos/robot.mp4')

while capture.isOpened():
    success,frame=capture.read()
    cv.imshow('Tesla Bot',frame)
    if cv.waitKey(60) & 0XFF==ord('d'):
        break