import cv2
import numpy as np
from matplotlib import pyplot as plt

image1 = cv2.imread('lena1.png')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

plt.subplot(2,3,1),plt.imshow(image1,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(thresh1,cmap = 'gray')
plt.title('Binario'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(thresh2,cmap = 'gray')
plt.title('Binario Invertido'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(thresh3,cmap = 'gray')
plt.title('Truncado'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(thresh4,cmap = 'gray')
plt.title('Truncado a zero'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(thresh5,cmap = 'gray')
plt.title('Truncado a zero INV'), plt.xticks([]), plt.yticks([])
plt.show()