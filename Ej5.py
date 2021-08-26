#Trabajar con listas
print("")
print("///Ejercicio 5///")
print("")
frutas = ["manzana", "banana", "frutilla"]
print("La lista original es: ", frutas)
print("El segundo elemento es: ", frutas[1])
for i in range(len(frutas)):
	if frutas[i]=="manzana":
		frutas[i]="kiwi"
frutas.append("naranja")
print(frutas)
limon = ["limon"]
frutas = frutas[:1] + limon + frutas[1:]
frutas.remove("banana")
print(frutas)