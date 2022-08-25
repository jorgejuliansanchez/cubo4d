print("editorc4d.py")

import cv2
import numpy as np
image = cv2.imread("Medellin4D_img.jpg")

puntos = np.array([])
points="212,230 217,228 227,237 233,232"
points=points.split()
for punto in points:
    punto=punto.replace(","," ")
    puntos = np.append(puntos, punto)	

print(puntos)
print(type(puntos))
print(puntos.shape)

#puntos = puntos.reshape((-1, 1, 2))
print(puntos)
print(type(puntos))
print(puntos.shape)


points = [[40, 109], [182, 343], [338, 345], [542, 292], [742, 322], [890, 221]]  
print(points)
print(type(points))
points = np.array(points)
print(points)
print(type(points))
print(points.shape)
points = points.reshape((-1, 1, 2))
print(points)
print(type(points))
print(points.shape)
color = (255, 0, 0)
thickness = 2
isClosed = False

image = cv2.polylines(image, [points], isClosed, color, thickness)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()