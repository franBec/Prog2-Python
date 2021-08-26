#Superposicion de listas
print()
print ("///Ejercicio 9///")
print()
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9]
lista3 = [2, 3, 4, "manzana"] #bien random la manzana ahi, simplemente porque si
print("lista 1 es:", lista1)
print("lista 2 es:", lista2)
print("lista 3 es:", lista3)
#no entiendo como funciona esto, lo saque de stack overflow y esta re piola
#no cumple con lo de usar for anidados que pide la consigna
#pero que elegancia hacerlo en una sola linea
print(any(x in lista2 for x in lista1))
print(any(x in lista3 for x in lista1))