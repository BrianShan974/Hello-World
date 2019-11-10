import matplotlib.pyplot as plt
from copy import deepcopy

image = []

def zero(image, width, height):
    image.clear()
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        image.append(row)

zero(image, 640, 640)

def upperLeftWhiteTriangle(image):
    image = deepcopy(image)
    for i in range(len(image)):
        image[i][:len(image) - i] = [255] * len(image[i][:len(image) - i])
    return image

plt.imshow(upperLeftWhiteTriangle(image), cmap='gray', vmin=0, vmax=255)
plt.show()