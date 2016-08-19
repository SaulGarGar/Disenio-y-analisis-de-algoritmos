#for c in range(5,10,2):
#	print (c)

alfabeto ="abcdefghijklmnopqrstuvwxyz"
contrasenia = "fa"
for l1 in alfabeto:
	for l2 in alfabeto:
		ca = l1+l2
		print (ca)
		if ca == contrasenia:
			print ("contrasenia invalida")


	