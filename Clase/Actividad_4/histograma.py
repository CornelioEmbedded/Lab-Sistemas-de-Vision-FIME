import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lena1.png")
histr = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(2, 1, 1)
plt.axis('off')
plt.imshow(img)
plt.title('Entrada / Input')

plt.subplot(2, 1, 2)
plt.plot(histr)
plt.title('Salida / Output')
plt.show()

plt.hist(img.ravel(),256,[0,256])
plt.show()
