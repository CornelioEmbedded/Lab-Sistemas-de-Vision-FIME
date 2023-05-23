from __future__ import print_function
from imutils.object_detection import non_max_suppression
import numpy as np 
import cv2 
import imutils

def facesAlgorithm(gray, frame):
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_classifier.detectMultiScale(frame, 1.099, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(127,0,255),2)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    scale = 1.0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    w = int(frame.shape[1] / scale)
    # frame = imutils.resize(frame, width=w)
    new_frame = imutils.resize(frame, width=min(500, frame.shape[1])) 
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # detect people in the image
    (rects, weights) = hog.detectMultiScale(new_frame, winStride=(8, 8),
                                            padding=(3, 3), scale=1.02)

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    for (xA, yA, xB, yB) in pick:
                cv2.rectangle(new_frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
    facesAlgorithm(gray, new_frame)

    cv2.imshow('frame', new_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()