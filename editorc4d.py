#EditorC4D
import cv2
import numpy as np

cam = cv2.VideoCapture(0)
width = cam.get(3)
height = cam.get(4)
nancho=int(512*width/height)
fx=int(nancho/2)
fy=256
x0=fx-192
x1=x0+384
y0=fy-192
y1=y0+384
sty=(0, 0, 255)

def poli4d(pid, pts, sty):
    points = pts.split()
    points = map(lambda p: tuple(map(int, p.split(','))), points)
    puntos=[]
    for point in points:
        puntos.append([point[0], point[1]])
    points = np.array(puntos, dtype=np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(image, [points], True, sty, 1)
    return 

def interfaz4d():
    mascara="106,237 120,343 139,410 170,468 212,497 248,509 295,507 349,487 387,459 421,416 449,367 460,297 450,226 429,112 386,61 332,29 271,15 221,35 186,62 143,114 118,151 104,201 106,237 "
    poli4d("mascara", mascara, sty)
    cuadro4d="64,64 448,64 448,448 64,448 64,64"
    poli4d("cuadro4d", cuadro4d, sty)
    return

while True:
    ret, frame = cam.read()
    if not ret:
        print("falla leyendo camara web")
        break
    frame = cv2.resize(frame, (nancho, 512))
    frame = cv2.flip(frame,1)
    image = np.random.randint(0,255,size=(512,512,3),dtype=np.uint8)
    interfaz4d()
    image[64: 448, 64: 448] = frame[y0:y1, x0:x1]
    cv2.imshow("EditorC4D", image)
    if cv2.waitKey(1) == ord('x'):
        break
    
cv2.destroyAllWindows()