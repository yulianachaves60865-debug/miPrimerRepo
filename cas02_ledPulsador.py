# llamar librerías:
import RPi.GPIO as GPIO

# Declarar Constantes:
PIN_BOTON = 3
PIN_LED = 7

# declarar variables:
estadoBoton = False

# zona de configuración:
GPIO.setmode(GPIO.BOARD) # desactivar mensajes de advertencias
GPIO.setwarnings(False)
GPIO.setup(PIN_BOTON, GPIO.IN)
GPIO.setup(PIN_LED, GPIO.OUT)

# zona de programa principal:
while True:
	estadoBoton = GPIO.input(PIN_BOTON) # Guardar el estado de la entrada en una variable

	if estadoBoton == True: # si el botón esta presionado, entonces:
		GPIO.output(PIN_LED, True) #encender LED
	print("PRESIONADO")
	else: # si el botón NO esta presionado, entonces
		GPIO.output(PIN_LED, False) # apagar LED
