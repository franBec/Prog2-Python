#Trabajar con listas
print()
print ("///Ejercicio 8///")
print()
lista = []
aux = int(input("ingrese numero: "))
while (aux%2 != 0):
	lista.append(aux)
	aux = int(input("ingrese numero: "))
print (lista)
