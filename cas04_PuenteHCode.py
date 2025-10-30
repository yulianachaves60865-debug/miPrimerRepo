# Llamar librerias:
import RPi.GPIO as GPIO # pines GPIO
from time import sleep # retardos

# Declarar Constantes:
PIN_IN1 = 7  # GPIO4
PIN_IN2 = 11 # GPIO17
PIN_IN3 = 13 # GPIO27
PIN_IN4 = 15 # GPIO22
PIN_ENA = 32 # Pin PWM
PIN_ENB = 33 # Pin PWM

# Declarar Variables:
maxSpeed = 100
minSpeed = 0

# Zona de Configuracion:
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # desactivar mensajes de advertencia
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_IN3, GPIO.OUT)
GPIO.setup(PIN_IN4, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)

# configurar pines PWM:
motorIzq = GPIO.PWM(PIN_ENA, maxSpeed)
motorDer = GPIO.PWM(PIN_ENB, maxSpeed)

# Habilitar pines PWM:
motorIzq.start(maxSpeed)
motorDer.start(maxSpeed)

# Zona Principal:
while True:
	motorIzq.ChangeDutyCycle(maxSpeed)
	motorDer.ChangeDutyCycle(maxSpeed)

	GPIO.output(PIN_IN1, True)  # giro Derecha motorIzq
	GPIO.output(PIN_IN2, False)
	GPIO.output(PIN_IN3, True)  # giro Derecha motorDer
	GPIO.output(PIN_IN4, False)
