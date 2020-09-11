import cv2
import os
import imutils

personName = 'yail'
dataPath = 'C:/Users/USUARIO/Desktop/PROYECTO UNIDAD I - RECONOCIMIENTO FACIAL CON MASCARILLAS/Data'
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
	print('Carpeta creada: ',personPath)
	os.makedirs(personPath)

cap = cv2.VideoCapture('yail.mp4')
#cap = cv2.VideoCapture(2) #parastreaming

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:

	ret, frame = cap.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
		count = count + 1
	cv2.imshow('Capturando rostro con mascarrilla',frame)
	k =  cv2.waitKey(1)
	if k == 27 or count >= 300:
		break

cap.release()
cv2.destroyAllWindows()