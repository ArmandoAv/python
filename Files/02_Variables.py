# Este archivo contendra el uso de las variables y constantes en python

# Las constantes en Python se les define con una nomenclatura en Mayusculas
# Esto es porque las constantes no existen como tal en Python
# Si el nombre es largo se usan guiones bajos para ir separando el nombre
# Algunos ejemplos pueden ser los dias de la semana, horas del dia
# Tambien puede ser valores matemticos como pi o valores que no van a cambiar

# Asignacion de constantes
HORAS_DIA = 24
DIAS_SEMANA = 7
LITROS = "4 lt"
NOMBRE = "Bart"
HOBBY = "andar en patineta"
NOM_PADRE = "Homero"

# Presentando las CONSTANTES
print(f"\n\nMi nombre es: {NOMBRE}")
print(f"Mi pasatiempo es: {HOBBY}")
print(f"Siempre estoy dispuesto las {HORAS_DIA} hr, los {DIAS_SEMANA} dias de la semana")
print(f"Mi padre {NOM_PADRE} siempre bebe {LITROS} de cerveza diario")

# Las variables en Python se les define con una nomenclatura en Minusculas
# Como su nombre lo dice, pueden ir variando sus valores dentro del programa
# Si el nombre es largo se usan guiones bajos para ir separando el nombre

# Asignacion de la variable nombre

nombre = "Admin"

# Presentando la variable
# Python distingue las Mayusculas de las Minusculas por este motivo es importante
# No nombrar una variable y una constante igual ya que puede provocar un error

print("\n\nA continuacion se obtendra el valor de la constante NOMBRE y la variable nombre")
print(f"El valor de la constante NOMBRE es: {NOMBRE}")
print(f"El valor de la variable nombre es:  {nombre}")
print("Los valores son diferentes debido a que Python discrimina entre Mayusculas y Minusculas")


# Asignacion de mas variables
nom_pila = "James"
ape_pat = "Earl"
ape_mat = "Jones"
pais = 'USA'
ciudad = 'Springfield'
edad = 60
casado = True
habilidad = ['HTML', 'CSS', 'JS', 'React', 'Python']

# Estos valores pueden ponerse como un diccionario
# Debido a que la variable es el diccionario
# No estamos repitiendo las mismas variables anteriores
inf_personal = {
                'Nombre':'Joe',
                'Apellido Paterno':'Doe',
                'Apellido Materno':'Downs',
                'Pais':'Canada',
                'Ciudad':'Ottawa',
                'Edad':35,
                'Casado':False,
                'Habilidades' : ['Linux','SQL','Airflow','ETL','MongoDB']
               }

# Presentando las variables
# A continuacion se vera una forma ademas de la cadena f
# Para presentar cadenas y variables esto es con la ayuda de la coma ,
# Este caracter le indica a la funcion print que esta concatenando

print("\n\nDatos personales del primer candidato\n")
print('Nombre:', nom_pila)
print('Apellido Paterno:', ape_pat)
print('Apellido Materno:', ape_mat)
# Se observa que el ocupar comilla simple o doble es indiferente
print("Pais:", pais)
print('Ciudad:', ciudad)
print('Edad:', edad)
print('Casado:', casado)
print('Habilidades:', habilidad)

print("\n\nDatos personales del segundo candidato\n")
print('Informacion personal:', inf_personal)

print("\n\nLos datos del segundo candidato fueron obtenidos desde un diccionario")
print("El problema con el diccionario es que presenta los datos como un formato JSON")
print("Por lo que no es muy atractivo visualmente, pero si solo se necesitan los datos")
print("Es una forma mas simple de llenar todos los datos en una sola variable")

# Concatenación de variables
# Como se observa en los casos anteriores tambien pueden concatenarse variables

print("\n\nConcatenamos el nombre y apellidos del primer candidato")
print(nom_pila,ape_pat,ape_mat)

nom_completo = nom_pila,ape_pat,ape_mat
print("Mi nombre completo es:",nom_completo)

# Longitud de cadena
long_ciudad = len(ciudad)
print("Mi ciudad es: ",ciudad)
print("Mi ciudad tiene", long_ciudad, "caracteres")

# Se pueden asignar varias variables en una sola linea
# Seguimos ocupando las variables ya declaradas anteriormente
# Para ver el concepto de como se puede ir cambiando el valor
nom_pila, ape_pat, ape_mat, edad, ciudad = "Jack", "Daniels", "III", 23, "Tequila"

# El print al concatenar puede escribirse en varias lineas
# Sin embargo los datos son devueltos en una sola linea
# Esto no puede hacerse con la cadena f
print("\n\nAsignamos un nuevo valor a las variables: nom_pila, ape_pat y ape_mat")
print("Esto para entender como pueden ir cambiando los valores de las variables")
print("Me llamo:", nom_pila, ape_pat, ape_mat,". Mi edad es:",
      edad,". Vivo en:", ciudad)

# Debido a que Python no asigna un tipo a las variables
# Una misma variable puede ocuparse para distintos tipos

nom_pila = "Homero"
print("\n\nAsignamos un nombre a la variable nom_pila, en este caso: ", nom_pila)
nom_pila = 38
print("Ahora le asignamos un numero a la variable nom_pila, en este caso: ", nom_pila)
print("\n\nDebido a que esto puede ser un problema, se recomienda al crear una variable")
print("Poner el tipo de dato que deseamos para esa variable, para evitar estos cambios")
print("Por ejemplo al crear la variable nom_pila hacerlo de la siguiente forma")
print("nom_pila: str = \"Homero\"")
print("Esto no evita que se pueda cambiar el tipo de la variable")
print("Pero indica el tipo de valor que se debe de respetar\n")
