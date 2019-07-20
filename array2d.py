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
    return (image, burnt)

def flip(image):
    new = [[]] * 6
    for row in range(len(image)):
        for index in range(len(image[row])):
            new[row].append(image[row][index-len(image[row])])
    return new

def clip(image, MaxVal):
    new = deepcopy(image)
    for row in range(len(new)):
        for pixel in range(len(new[row])):
            if new[row][pixel] > MaxVal:
                new[row][pixel] = MaxVal
    return new
