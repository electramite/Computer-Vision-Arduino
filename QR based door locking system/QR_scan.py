import cv2
import numpy as np
import serial
import time
from pyzbar.pyzbar import decode
 

cap = cv2.VideoCapture(0) # open webcam
cap.set(3,640) # setting width of output window
cap.set(4,480) # setting height of output window

arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1) # using COM port 8 with baud rate of 9600

def write_read(x):
    arduino.write(bytes(x, 'utf-8')) # converting 'x' into bytes with an utf-8 encoding

while True:
 
	success, img = cap.read() # capturing images from camera

	for barcode in decode(img):
		myData = barcode.data.decode('utf-8') # if barcode present, reading & extracting data from barcode
		#print(myData) # printing barcode decoded text
		if myData=="Electramite": # if barcode encoded text is 'Electramite'
			write_read("1") # opening the door by sending '1' to arduino

		# plotting square around barcode and printing text on the captured image
		pts = np.array([barcode.polygon],np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img,[pts],True,(255,0,255),5)
		pts2 = barcode.rect
		cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
		0.9,(255,0,255),2)
	 
	cv2.imshow('Result',img) # showing captured image 
	cv2.waitKey(1)
