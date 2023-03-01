import matplotlib.pyplot as plt
import numpy as np
import cv2
import practica_1

practica_1.make_image_scale(r'fotos\foto_6.png', 8)

sample_image = cv2.imread('scaled.png')

twoDimage = sample_image.reshape((-1,3))
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
attempts=10

ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((sample_image.shape))

cv2.imwrite('result_3.png', result_image)