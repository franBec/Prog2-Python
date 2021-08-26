#Slice string y comparar con lista
print()
print ("///Ejercicio 16///")
print()
mail = str(input("Ingrese mail: "))
usuario = mail[:mail.index('@')]
dominio = mail[mail.index('@')+1:mail.index('.')]
extension = mail[mail.index('.')+1:]
print("usuario: ",usuario)
print("dominio: ",dominio)
print("extension: ",extension)
dominiosValidos = ["gmail", "hotmail", "outlook", "manzana"] #si, manzana
if dominio in dominiosValidos:
	print("Direccion válida")
else:
	print("Direccion inválida")