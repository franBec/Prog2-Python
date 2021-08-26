#Funciones, string
print()
print ("///Ejercicio 18///")
print()
#funcion del ejercicio 14
def alVerre(string):
	return string[::-1]

string = str(input("Ingrese palabra: "))
if string==alVerre(string):
	print(string, "es palindromo")
else:
	print(string, "no es palindromo")