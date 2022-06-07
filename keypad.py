import Adafruit_BBIO.GPIO as GPIO
import time

Filas = [1,2,3,4]

Filas[0] = "P9_15"
Filas[1] = "P9_23"
Filas[2] = "P9_25"
Filas[3] = "P9_27"

GPIO.setup(Filas[0], GPIO.OUT)
GPIO.setup(Filas[1], GPIO.OUT)
GPIO.setup(Filas[2], GPIO.OUT)
GPIO.setup(Filas[3], GPIO.OUT)

Columnas = [5,6,7,8]

Columnas[0] = "P8_11"
Columnas[1] = "P8_12"
Columnas[2] = "P8_15"
Columnas[3] = "P8_17"

GPIO.setup(Columnas[0], GPIO.IN)
GPIO.setup(Columnas[1], GPIO.IN)
GPIO.setup(Columnas[2], GPIO.IN)
GPIO.setup(Columnas[3], GPIO.IN)

def lectura(FILAS,CARACTERES):
	#EnFilas = FILAS
	#GPIO.output(EnFilas, GPIO.HIGH)
	GPIO.output(FILAS, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(Columnas[0]):
		print(CARACTERES[0])
		#GPIO.output(FILAS, GPIO.LOW)
		#return
	time.sleep(0.1)
	if GPIO.input(Columnas[1]):
		print(CARACTERES[1])
		#GPIO.output(FILAS, GPIO.LOW)
		#return
	time.sleep(0.1)
	if GPIO.input(Columnas[2]):
		print(CARACTERES[2])
		#GPIO.output(FILAS, GPIO.LOW)
		#return
	time.sleep(0.1)
	if GPIO.input(Columnas[3]):
		print(CARACTERES[3])
		#GPIO.output(FILAS, GPIO.LOW)
		#return
	time.sleep(0.1)
	#GPIO.output(EnFilas, GPIO.LOW)
	GPIO.output(FILAS, GPIO.LOW)
	return
try:
	while True:
		lectura(Filas[0],["1","2","3","A"])
		#time.sleep(0.5)
		lectura(Filas[1],["4","5","6","B"])
		#time.sleep(0.5)
		lectura(Filas[2],["7","8","9","C"])
		#time.sleep(0.5)
		lectura(Filas[3],["*","0","#","D"])
		#time.sleep(0.5)
except KeyboardInterrupt:
	print("\Fin")
