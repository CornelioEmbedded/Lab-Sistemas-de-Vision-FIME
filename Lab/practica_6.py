import numpy as np
import cv2

#Creamos nuestro canvas negro
image = np.zeros((512,512,3), np.uint8)

cv2.line(image, (100,100), (370,420), (0,0,255), 9)

# Grosor 
cv2.rectangle(image, (100,100), (300,250), (127,50,127), 10)

#Creamos nuestro circulo
cv2.circle(image, (250, 250), 150, (15,150,50), 1) 

# Definimos nuestros puntos
pts = np.array( [[10,120], [400,300], [90,200], [120,500]], np.int32)

# Cambiamos la forma de nuestros puntos a la forma requerida por la funcion
pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True , (0,0,255), 3)

#Escribimos el texto que queramos que aparezca en la imagen
ourString =  'FIME'
#Utilizamos la función
cv2.putText(image, ourString, (155,290), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (40,200,0), 4)
#Mostramos el resultado
cv2.imshow("Imagen con texto", image)
cv2.waitKey(0)
cv2.destroyAllWindows()