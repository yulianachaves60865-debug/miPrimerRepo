vs = 20 # voltios
Rs = 75 # ohmios
Ro = 100 # ohmios
k = 0.5 # adimencional
done = 1 #valor centinela

while done:
	vm = float(input("ingrese el vultaje mostrado en el multimero: "))

	if vm >= 12.0 and vm <= 18.0 # si vm esta entre 12 y 18, entonces:
		T = (Rs/k) * (vm/(vs-vm)) - (Ro/k) # Formunla de la temperatura de la camara
		print("La temperatura d ela camara de gas es: ",T)
		done = 0 # desactivar centinela
	else:
		print("voltaje incorrecto. Por favor ingrese nuevamente el valor.")
