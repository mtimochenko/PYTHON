#Arrays
# variable = ""
dias_semana = ["lunes","martes","miercoles","jueves","viernes"]
datoArrayX = "hola"
arrayX = ["franco",19,True, datoArrayX]
# Array o Vector : Unidimensional
#print(dias_semana[0])
#print(dias_semana[2])
# Array tiene posiciones
agregar_opcion = int(input("Desea ingresar un dia nuevo a la semana de trabajo? 0 si no , 1 si deseas agregar"))
if(agregar_opcion == 0):
         print("No se agregan dias nuevos , continuamos")
else:
         dia_nuevo = input("Cual es el nombre del dia que deseas ingresar?")
         
         dias_semana.append(dia_nuevo) #ingresa en la ultima posicion del array el valor
         # de la variable que se pasa entre parentesis
         #dias_semana.pop()
         

# ["f","r","a","n","c","o"]
# Saber la cantidad de elementos que tiene un array o una variable en general
# Recorrer elementos
# Imprimir todos los elementos del array dias_semana
for i in range(len(dias_semana)):
         print(dias_semana[i])
         if(dias_semana[i] == "sabado"):
                  print("Sale joda")

