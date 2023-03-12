import cv2

image = cv2.imread(r'fotos\figurasColores2.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
edges = cv2.Canny(gray_image, 10, 150)
dilatate = cv2.dilate(edges, None, iterations=1)
erode = cv2.erode(dilatate, None, iterations=1)
contourns , _ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

figure = str(input('Que figura quiere encontrar?: '))
figures = {'triangulo': 3,
           'cuadrado': 4,
           'rectangulo': 4,
           'pentagono': 5,
           'hexagono': 6,
           'circulo': 10}

for contourn in contourns:
    epsilon = 0.01 * cv2.arcLength(contourn, True)
    approx = cv2.approxPolyDP(contourn, epsilon, True)
    x,y,w,h = cv2.boundingRect(approx)

    if len(approx) in figures.values():
        if figures[figure] == len(approx):
            cv2.putText(image, figure, (x,y-5),1,1,(0,255,0),1)
    else:
        if figure == 'circulo':
            cv2.putText(image, figure, (x,y-5),1,1,(0,255,0),1)


cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
