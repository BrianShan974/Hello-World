from copy import deepcopy

def lighten(image):
    burnt = False
    new = deepcopy(image)
    for row in range(len(new)):
        for pixel in range(len(new[row])):
            new[row][pixel] *= 1.1
            if new[row][pixel] > 254.5:
                burnt = True
            new[row][pixel] = round(new[row][pixel])
    return burnt

def flip(image):
    new = [[]] * 6
    for row in range(len(image)):
        for index in range(len(image[row])):
            new[row].append(image[row][index-len(image[row])])
    return [new[1][0:8],new[1][8:17],new[1][17:25],new[1][25:]]

def clip(image, MaxVal):
    new = deepcopy(image)
    for row in range(len(new)):
        for pixel in range(len(new[row])):
            if new[row][pixel] > MaxVal:
                new[row][pixel] = MaxVal
    return new

def printimage(image):
    for i in image:
        print(i)

image = [[80,80,255,80,80,255,80,80],[80,80,255,80,80,255,80,80],[255,80,120,120,120,120,255,80],[255,80,255,255,255,255,80,80],[255,80,120,120,120,120,80,80]]

print("lighten")
print(lighten(image))
print("flip")
printimage(flip(image))
print("clip 100")
printimage(clip(image, 200))