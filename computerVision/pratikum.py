import cv2
import numpy as np

#tahap 2
img = cv2.imread('tes.png')
print(type(img))
print(img.shape)

#tahap 3
cv2.imshow('Usup Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#tahap 4
pixel = img[100, 150]
print("Nilai piksel (BGR):", pixel)
# Akses satu channel saja:
blue = img[100, 150, 0]
print("Channel Biru:", blue)

