# Processing images

import matplotlib.image as img
import numpy as np
from PIL import Image

IMAGE = "foto_4.png"

def make_image_scale(photo:str, scale):
    image = img.imread(photo)
    w, h = image.shape[:2]

    xNew = int(w * 1 / scale)
    yNew = int(h * 1 / scale)

    xScale = xNew/(w-1)
    yScale = yNew/(h-1)

    newImage = np.zeros([xNew, yNew, 4])

    for i in range(xNew-1):
        for j in range(yNew-1):
            newImage[i + 1, j + 1]= image[1 + int(i / xScale), 1 + int(j / yScale)]

    np.set_printoptions(threshold=np.inf)
    img.imsave('scaled.png', newImage)

def get_matrix():
    new_image = Image.open("scaled.png")
    image_array = np.array(new_image)
    row = []
    matrix=[]
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            pixel_value = image_array[i, j]
            row.append(pixel_value[3])
        matrix.append(row)

    with open('matrix.txt', 'w') as file:
        file.write(str(matrix))

make_image_scale(IMAGE, 10)
get_matrix()


