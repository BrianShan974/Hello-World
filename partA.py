from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("img.jpeg")

oneBitOfNothingness = img.convert("1")
eightBitsOfGray = img.convert('L')
twentyFourBitsOfColor = img.convert("RGB")
thirtyTwoBitsOfColorAndTransparency = img.convert("RGBA")

plt.figure("partA")
plt.subplot(2,3,1)
plt.imshow(oneBitOfNothingness),plt.axis('off')
plt.subplot(2,3,2),
plt.imshow(eightBitsOfGray),plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(twentyFourBitsOfColor),plt.axis('off')
plt.subplot(2,3,4)
plt.imshow(thirtyTwoBitsOfColorAndTransparency), plt.axis('off')
plt.show()