# Este es un archivo con la funcion print y algunas de sus caracteristicas

# Este es un comentario
# de varias lineas

"""
Este tambien es un
comentario de
varias líneas
"""

'''
Este tambien es un
comentario de
varias líneas
'''

# Con la funcion print se va a monstrar el texto al ejecutar un programa en Python
# Se puede agregar en blanco si se desea un salto de linea
print()
print('Se puede imprimir una cadena con comillas simples')
print("Se puede imprimir una cadena con comillas dobles")
print()

# Con la funcion input se puede agregar algun valor desde el teclado
# Si agregamos la funcion a una variable
# Al ejecutar el programa nos pone el cursor para poder ingrear un valor
# En una linea diferente
print("Se solicita una cadena para continuar con la ejecucion del programa: ")
cad_f = input()

# Para imprimir el valor de la variable se puede ocupar print
# Si se pone una f al principio, ha esto se le conoce como cadena f
# Sirve para sustituir el valor de las variables y expresiones
# Que estan entre corchetes {}, siempre va una f antes de las comillas ""
# Imprime el valor tecleado, asi como la cadena que ponemos
print(f"La cadena ingresada es: {cad_f}")

# Si solo queremos imprimir el valor de la variable
# No es necesario la cadena f ni los corchetes {}
print('La cadena ingresada tambien puede imprimirse sin necesidad de ninguna otra cadena')
print(cad_f)

# Imprime la cadena y ademas espera el valor desde el teclado
# El cursor queda en la misma linea del teclado
val_f = input("Se solicita otra cadena para continuar con la ejecucion del programa: ")
# Imprime la cadena y ademas el valor tecleado con la cadena f
print(f"La nueva cadena ingresada es: {val_f}")
print()

# La funcion int ayuda con los numeros enteros (positivos y negativos)
# Se puede ocupar agregando una cadena con la funcion input
# Al final solo devolvera el numero entero sin importar si hay alguna cadena
# Estas lineas mandan la peticion al teclado para un numero entero
# Ademas imprimen el numero entero tecleado
num_1 = int(input("Se solicita un numero entero para continuar con la ejecucion del programa: "))
print(f"El numero entero ingresado fue:  {num_1}")
print()

# La funcion float ayuda con los numeros reales (positivos y negativos)
# Se puede ocupar agregando una cadena con la funcion input
# Al final solo devolvera el numero real sin importar si hay alguna cadena
# Estas lineas mandan la peticion al teclado para un numero real
# Ademas imprimen el numero real tecleado
num_2 = float(input("Se solicita un numero real para continuar con la ejecucion del programa: "))
print(f"El numero real ingresado fue:  {num_2}")
print()

# La funcion bool ayuda con los valores booleanos
# Se puede ocupar agregando una cadena con la funcion input
# Al final solo devolvera el valor booleano sin importar si hay alguna cadena
# Estas lineas mandan la peticion al teclado para un valor booleano
# Ademas imprimen el valor booleano tecleado
bol_1 = bool(input("Se solicita un valor booleano para continuar con la ejecucion del programa: "))
print(f"El valor boleano ingresado fue:  {bol_1}")
print()

# La funcion str ayuda con las cadenas
# Estas lineas mandan la peticion al teclado para una cadena
# Ademas imprimen el valor de la cadena tecleada
cad_1 = str(input("Se solicita un comentario para continuar con la ejecucion del programa: "))
print(f"El comentario agregado es: {cad_1}")
print()

# Estas lineas imprimen los valores en una sola linea
# Esto se logra poninedo un valor diferente al final de la cadena con end
# Cuando no se agrega nigun valor al final para end se toma por default
# Un salto de linea, en este caso el valor final de la cadena es
# Una coma y un espacio en blanco
print("La siguiente cadena fue codificada en dos sentencias separadas")
print("Primera parte de la cadena", end=", ")
print("segunda parte de la cadena")
print()

# Esta linea imprime los valores en varias lineas con ayuda del salto 
# De linea \n y tabula con ayuda del tabulador \t
print("La siguientes cadenas fueron codificadas en una sola sentencia")
print("\nEsto es una lista de personas \nNombre\tApellido\nJoe\tDoe\nBart\tSimpson\nPeter\tGrifin\n")

print("Las siguientes cadenas imprimen algunos caracteres especiales")
# Esta linea imprime los valores de salto de linea \n y del tabulador \t
print("\nSe requiere imprimir los valores de salto de linea \\n y de tabulador \\t")

# Esta linea imprime los valores de caracteres especiales como comillas dobles o simples
print("Se requiere imprimir los valores de \"comillas dobles\" y de \'comillas simples\'")

# A continuacion se vera un ejemplo para poner una cadena al reves
# Se pide una cadena como en los ejemplos anteriores pero la funcion
# Input se pone vacia para que el resultado se mas facil de ver
# Para lograr que la cadena quede al reves se ocupan los corchetes
# Los primeros valores se quedan en blanco y el ultimo valor se pone -1
# Esta funcionalidad se vera con mas detalle mas adelante
print("\nLa siguiente cadena se imprimira al reves: ")
cad_2 = input()
print(f"{cad_2[::-1]}")

# Para consultar el tipo de dato que se tiene se ocupa la funcion type
# Si se ocupa la funcion type despues de un print el resultado es que 
# El tipo de dato no tiene un valor asignado NoneType
# Si solo son numeros no es necesario poner comillas en la funcion print
print("\nLas siguientes cadenas se obtendran sus respectivos tipos de datos que hay en Python")
print("\nHola Mundo")
print(type("Hola Mundo"))
print(5553259000)
print(type(5553259000))
print(1234.5678)
print(type(1234.5678))
print(123 + 321j)
print(type(321 + 123j))
print("True")
print(type(True))
print([1, 2, 3, 4, 5])
print(type([1, 2, 3, 4, 5]))
print({'nombre':'Bart','apellido':'Simpson','edad':10})
print(type({'nombre':'Bart','apellido':'Simpson','edad':10}))
print({9.98, 3.1416, 2.754})
print(type({9.98, 3.1416, 2.754}))
print((9.98, 3.1416, 2.754))
print(type((9.98, 3.1416, 2.754)))
print(type(print("Mi cadena de texto, en este caso se agrego la funcion print anidada en type")))
print("\nSe puede apreciar que el tipo de dato en la primer cadena y en la ultima no son iguales")
print("Esto es debido a que se acomodaron las funciones print y type de forma diferente")
print("Obteniendo en la primer cadena un tipo string y en la segunda no se tiene una tipificacion")
print("Este resultado es porque print es una funcion y no tiene una tipificacion")
print("Por lo que no importa el tipo de dato dentro del print, siempre sera NoneType\n")
