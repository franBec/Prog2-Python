#Funciones
print()
print ("///Ejercicio 12///")
print()

def palabraMasLarga(palabras = []):
	aux = ""
	for i in range(len(palabras)):
		if len(aux)<len(palabras[i]):
			aux = palabras[i]
	return aux

lista1 = ["bokita", "el", "mas", "grande"]
print("el mas grande es: ", palabraMasLarga(lista1))