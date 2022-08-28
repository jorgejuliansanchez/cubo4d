#EditorC4D
import cv2
import numpy as np
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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
sty=(0, 0, 0)

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
    poli4d("mascara", mascara, sty)
    cuadro4d="64,64 448,64 448,448 64,448 64,64"
    poli4d("cuadro4d", cuadro4d, sty)
    poli4d("l1", "0,0 64,64 ", sty)
    poli4d("l2", "512,0 448,64 ", sty)
    poli4d("l3", "512,512 448,448 ", sty)
    poli4d("l4", "0,512 64,448 ", sty)
    return
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while True:
        ret, frame = cam.read()
        if not ret:
            print("falla leyendo camara web")
            break
        imagen = np.random.randint(0,255,size=(512,512,3),dtype=np.uint8)        
        frame = cv2.resize(frame, (nancho, 512))
        frame = cv2.flip(frame,1)
        v384=frame[y0:y1, x0:x1]
        imagen[64: 448, 64: 448] = v384
        interfaz4d()
        #gray = cv2.cvtColor(v384, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.3, 1)
        #for (x,y,w,h) in faces:
        #    cv2.rectangle(imagen,(x+64,y+64),(x+64+w,y+64+h),(0,255,0),1)
        image = cv2.cvtColor(v384, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = face_mesh.process(image)
        if results.multi_face_landmarks:
          for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=imagen,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
        cv2.imshow("EditorC4D", imagen)
        if cv2.waitKey(1) == ord('x'):
            break
        
cv2.destroyAllWindows()