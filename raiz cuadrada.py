#Busqueda exaustiva = probar cada una de las soluciones

numero = int(input("escribe un numero"))
raiz = 0.0
incremento = 1

for i in range(5):
	while raiz*raiz < numero:
		
		raiz = raiz + incremento

		raiz = raiz - incremento
		incremento = incremento / 10



print (raiz)
