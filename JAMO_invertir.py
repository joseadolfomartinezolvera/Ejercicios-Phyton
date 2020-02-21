palabra = raw_input("Ingrese una frase: ")
 
d = 1
a = len(palabra)
 
while d < a:
	print palabra[-d]
	d += 1
 
input("")
