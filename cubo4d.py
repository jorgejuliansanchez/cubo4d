#Cubo4D
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
x=0
y=0
def poli4d(pid, pts, sty):
    points = pts.split()
    points = map(lambda p: tuple(map(int, p.split(','))), points)
    puntos=[]
    for point in points:
        puntos.append([point[0], point[1]])
    points = np.array(puntos, dtype=np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(imagen, [points], True, sty, 1)
    return 
def interfaz4d():
    mascara="255,448 255,399 255,352 256,304 256,272 256,240 256,204 256,160 209,161 161,174 133,208 126,256 133,208 161,174 209,161 256,160 303,163 350,176 379,205 385,256 379,205 350,176 303,163 256,160 256,111 256,64 208,68 160,112 135,160 128,208 126,256 132,303 150,352 177,399 208,425 255,448 304,424 334,398 366,352 380,304 385,256 384,208 376,160 352,112 303,69 256,64"
    poli4d("mascara", mascara, (0, 0, 255))
    poli4d("cuadro4d", "64,64 448,64 448,448 64,448 64,64", (0, 0, 255))

    return
while True:
    ret, frame = cam.read()
    if not ret:
        print("falla leyendo camara web")
        break
    #imagen = np.random.randint(0,255,size=(512,512,3),dtype=np.uint8)        
    imagen = np.zeros([512,512,3],dtype=np.uint8)
    imagen.fill(255)
    frame = cv2.resize(frame, (nancho, 512))
    frame = cv2.flip(frame,1)
    v384=frame[y0:y1, x0:x1]
    norte=v384[0:192, 0:384]
    src = np.array([[0, 0], [384 , 0], [384 , 192 ], [0, 192]], dtype=np.float32)
    dst = np.array([[64, 448], [448, 448], [512, 512], [0, 512]], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(src,dst)
    result = cv2.warpPerspective(norte, matrix, (512,512))
    imagen[0: 512, 0: 512] = result
    
    sur=v384[192:384, 0:384]
    cv2.imshow("sur", sur)
    este=v384[0:384, 192:384]
    cv2.imshow("este", este)
    oeste=v384[0:384, 0:192]
    cv2.imshow("oeste", oeste)

    dst = np.array([[0, 0], [512, 0], [448, 64], [64, 64]], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(src,dst)
    result = cv2.warpPerspective(v384, matrix, (512,512))
    imagen = cv2.add(imagen,result)
    imagen[64: 448, 64: 448] = v384
    x=x+1
    y=y+1
    if x<64:
        poli4d("l1", "0,0 " +str(x)+","+str(y), (0, 0, 255))
        poli4d("l2", "512,0 " +str(512-x)+","+str(y), (0, 0, 255))
        poli4d("l3", "512,512 " +str(512-x)+","+str(512-y), (0, 0, 255))
        poli4d("l4", "0,512 " +str(x)+","+str(512-y), (0, 0, 255))
    else:
        poli4d("l1", "0,0 64,64", (0, 0, 255))
        poli4d("l2", "512,0 448,64 ", (0, 0, 255))
        poli4d("l3", "512,512 448,448 ", (0, 0, 255))
        poli4d("l4", "0,512 64,448 ", (0, 0, 255))
    interfaz4d()
    cv2.imshow("Cubo4D", imagen)
    if cv2.waitKey(1) == 27:
        break
        
cv2.destroyAllWindows()