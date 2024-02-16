# Solicitar al usuario que introduzca datos
resultado = input("Ingresa tu edad:")
# Determinar el tipo de una variable
print(type(resultado))

# Realizar casting de datos 
numUser = int(resultado)

print(numUser + 5)

# otros ejemplos: 
str(22)
float("22.15")
bool("un string") # --> Casi siempre arroja true

# Solo hay 4 excepciones para hacer que devuelva false
bool("False")
bool("0")
bool("")
bool("None") 