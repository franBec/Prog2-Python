#Trabajar con listas
print()
print ("///Ejercicio 10///")
print()
lista = []
#aca haria un do while pero no existe eso en Python
#DATAZO tampoco existe i++, hay que hacer i+=1
#o si queres secar la mente, i-=-1 funciona tambien :D
cant = int(input("Cuantas palabras vas a ingresar: "))
while cant<=0:
	print("Valor incorrecto. Ingrese nuevamente")
	cant = int(input("Cuantas palabras vas a ingresar: "))
for i in range(cant):
	lista.append(str(input("Ingrese palabra: ")))
print("La lista tiene", cant, "palabras. Estas son: ", lista)
#me pinto ver como unia todo en un string
string = "".join(lista)
print (string)