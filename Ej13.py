#Funciones, contar repeticiones y tuplas
print()
print ("///Ejercicio 13///")
print()

def empaquetarEnTuplas(lista = []):
	return [(x,lista.count(x)) for x in set(lista)] #codigo sacado de StackOverflow
	
lista1 = [1,1,1,3,5,1,1,3,3]
lista1 = empaquetarEnTuplas(lista1)
print(lista1)