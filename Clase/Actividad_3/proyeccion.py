import cv2
import numpy as np

image = cv2.imread('Ave_2.jpg')

pts1 = np.float32([[0, 0], [640, 0],[0, 640], [640, 640]])
pts2 = np.float32([[700, 0], [1000, 0],[0, 500], [800, 800]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))

imageOut = cv2.imwrite('result2.png', result)
