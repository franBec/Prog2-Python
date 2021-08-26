#Listas, tuplas, diccionario
print()
print ("///Ejercicio 19///")
print()
#No estoy 100% seguro de porque funciona. Saque la funcion de StackOverflow
def insertarEnDiccionario(clave, valor, diccionario):
	if not clave in diccionario:
		diccionario[clave] = [(valor)]
	else:
		diccionario[clave].append((valor))

d = {}
lista = [('Pedro', 2664889665), ('Pedro', 2665366998), ('Juan', 2657503689)] 
for i in range(len(lista)):
	x,y=lista[i]
	insertarEnDiccionario(x, y, d)
print(d)
