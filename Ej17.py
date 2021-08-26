#funcion random y recursividad
print()
print ("///Ejercicio 17///")
print()

def advinanza(random,guess,lifes):
	if random==guess:
		print("Ganaste")
	elif lifes == 0:
		print("Perdiste. El numero era ",random)
	elif random<guess:
		print("Numero random es menor, te quedan", lifes, "chances. Intente nuevamente")
		guess = int(input())
		advinanza(random,guess,lifes-1)
	else:
		print("Numero random es mayor, te quedan", lifes, "chances. Intente nuevamente")
		guess = int(input())
		advinanza(random,guess,lifes-1)

import random
random = random.randint(1,9)
lifes = 3
print("Se genero un numero random entre 1 y 9. Adivine cual es. Tenes", lifes, "chances: ")
guess = int(input())
advinanza(random,guess,lifes-1)
