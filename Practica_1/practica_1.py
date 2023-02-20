# using matplotlib and numpy

import matplotlib.image as img
import numpy as np

# provide the location of image for reading
image = img.imread("foto_5.png")

# determining the length of original image
w, h = image.shape[:2]
print(f'Width: {w}, Height: {h}')

# xNew and yNew are new width and
# height of image required
# after scaling
xNew = int(w * 1 / 10)
yNew = int(h * 1 / 10)

# calculating the scaling factor
# work for more than 2 pixel
xScale = xNew/(w-1)
yScale = yNew/(h-1)

# using numpy taking a matrix of xNew
# width and yNew height with
# 4 attribute [alpha, B, G, B] values

newImage = np.zeros([xNew, yNew, 4])
print(f'Width: {xNew}, Height: {yNew}')

for i in range(xNew-1):
    for j in range(yNew-1):
        print(image[1 + int(i / xScale), 1 + int(j / yScale)])
        newImage[i + 1, j + 1]= image[1 + int(i / xScale), 1 + int(j / yScale)]

# np.save('matrix.npy', newImage)
np.set_printoptions(threshold=np.inf)
# matrix = str(np.load('matrix.npy'))
# with open('matrix.txt', 'w') as f:
#     f.write(matrix)
# Save the image after scaling
img.imsave('scaled.png', newImage)
