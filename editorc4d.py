import cv2
import numpy as np

def poli4d(pid, pts, sty):
    points = pts.split()
    points = map(lambda p: tuple(map(int, p.split(','))), points)
    puntos=[]
    for point in points:
        puntos.append([point[0], point[1]])
    points = np.array(puntos, dtype=np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(image, [points], 1, sty, 1)
    return 

image = np.zeros((512,512,3), np.uint8)
sty=(0, 255, 0)
points="106,237 120,343 139,410 170,468 212,497 248,509 295,507 349,487 387,459 421,416 449,367 460,297 450,226 429,112 386,61 332,29 271,15 221,35 186,62 143,114 118,151 104,201 106,237 "
poli4d("image", points, sty)
points="64,64 448,64 448,448 64,448 64,64"
poli4d("image", points, sty)
cv2.imshow("EditorC4D", image)
cv2.waitKey(0)
cv2.destroyAllWindows()