#Calcular número de pulsaciones
#Condicional 2
#Autor Darien Asdrwal Pesca Ojeda
#Fecha 27/07/2022
#Declaración de variables
edad=0
genero=""

#Solicitud de datos por teclado
edad=int(input("Digite su edad: "))
genero=(input("Digite su genero, F para femenino, M para masculino: "))

#Procesos
if(genero=="F"):
    pulsaciones=(220-edad)/10
    print("Las pulsaciones por cada 10 segundos de ejercicio son de:",pulsaciones)

elif(genero=="M"):
    pulsaciones=(210-edad)/10
    print("Las pulsaciones por cada 10 segundos de ejercicio son de:",pulsaciones)
else:
    print("Recuerde que solo se permite F o M en mayúscula")