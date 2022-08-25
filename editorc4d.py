print("editorc4d.py")

import cv2
import numpy as np
image = cv2.imread("Medellin4D_img.jpg")
points="106,237 120,343 139,410 170,468 212,497 248,509 295,507 349,487 387,459 421,416 449,367 460,297 450,226 429,112 386,61 332,29 271,15 221,35 186,62 143,114 118,151 104,201 106,237 "
points = points.split()
points = map(lambda p: tuple(map(int, p.split(','))), points)
puntos=[]
for point in points:
  puntos.append([point[0], point[1]])

points = np.array(puntos, dtype=np.int32)
points = points.reshape((-1, 1, 2))
color = (0, 255, 0)
thickness = 1
isClosed = False

image = cv2.polylines(image, [points], isClosed, color, thickness)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
