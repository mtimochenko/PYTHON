print("Hola mundo")
numero1 = 4
numero2 = 8
nombre = "Franco"
resultado_suma = 0
resultado_division = 0
resultado_potencia = 0
resultado_multiplicacion = 0
edad_usuario = 1

print("Bienvenido : ")
print(nombre)
print("Numero 1 : ", numero1, " numero 2: ", numero2, " entendiste : ", nombre, "?" )
#resultado_suma = numero1 + numero2
#resultado_division = numero2/numero1
#resultado_potencia = numero1 ** numero2
#resultado_multiplicacion = numero1 * numero2
#nombre_usuario = input("Ingrese su nombre")
# Esto es un comentario
#edad_usuario = int(input( "Ingresa tu edad " ))

#print("Hola ", nombre_usuario, " tu edad es : ", edad_usuario)

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
sueldo = float(input("Ingrese el sueldo"))
# Operadores Matematicos
#5 > 3
#4 < 8 
#4 = 4
if(edad > 18 and nombre == "franco"):
	print("Bienvenido : " , nombre)
	if(sueldo >= 900):
		print("Sueldo mayor o igual a 900")
	else :
		print("Sueldo menor a 900")

else:
	print("O no sos mayor de edad o no sos franco")


