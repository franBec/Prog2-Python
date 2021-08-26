#Trabajar con listas
print()
print ("///Ejercicio 11///")
print()
lista1=[1,5,12,7,9,6,5]
lista2=[1,5]
lista3=[]
print ("Lista 1: ",lista1)
print ("Lista 2: ",lista2)
for int in lista1:
	if int not in lista2:
			lista3.append(int)
print ("Resultado: ",lista3)