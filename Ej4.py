#Operaciones con string
print("")
print("///Ejercicio 4///")
print("")
string = str(input("Ingrese frase: "))
print(string[1])
print(string[1:4])
print(string.replace(" ", "")) #funciono de pedo
print(len(string))
print(string.lower())
print(string.upper())

#Esta idea no funciona porque "replace" trabaja strings, no caracteres

#caracter1= str(input("Letra a reemplazar: "))
#caracter2 = str(input("Nueva letra: "))
#print (string.replace("caracter1", "caracter2"))

#como strings son inmutables, si hay que cambiar algo, castearlo a lista
caracter1= str(input("Letra a reemplazar: "))
caracter2 = str(input("Nueva letra: "))
lista = list(string)
for i in range(len(lista)):
	if (lista[i]==caracter1):
		lista[i]=caracter2
print("".join(lista))
isSubstring = str(input("Ingrese cosa para ver si es substring del string original: "))
print (isSubstring in string)