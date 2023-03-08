import cv2
import numpy as np

image = cv2.imread('portada.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

TRAS_X = 600
TRAS_Y = 10

# Traslación
M = np.float32([[1,0,TRAS_X],[0,1,TRAS_Y]])
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imwrite('result.png', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()
