import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('img/wireframe-two.png')
img_gray =cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('img/wireframe-two-header.jpg', 0)

h, w = template.shape[::]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
plt.imshow(res, cmap='gray')

threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
  cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] +h), (0, 0, 255), 2)

cv2.imshow("Matched Image", img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
