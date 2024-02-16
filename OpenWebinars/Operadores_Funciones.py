# Funciones incorporadas:

# 1. print()
print("Hola, mundo!")

print("Hola son las" + str(6) + "de la tarde") # unificar cadenas de caracteres 

print("Hola son las", 6,  "de la tarde")

print("%d %f %s" % (2.5, 2.5, 2.5))

# resultado-->  2, 2.5000000 2.5

    # %d --> entero
    # %f --> real
    # %s --> string

# permiter formatear la salida
print("El producto %s cantidad=%d precio=%.2f" 
      % 
      ("cesta",         23,          13.456))
    # reslutado --> El producto cesta cantidad=23 precio=13.46    

print("abc" * 3)
    # reslutado -->  'abcabcabc'

# 2. len()

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Salida: 5 --> indica la cantidad de valores de la lista o de un string

    # devuelve un valor entero

# 3. input()
name = input("¿Cuál es tu nombre? ") # leer informacion que inserta el user
print("Hola,", name)

# 4. range()
for i in range(5):
    print(i)

# 5. type()
x = 5
print(type(x))  # Salida: <class 'int'>  NOS DICE DE QUE TIPO ES ESA VARIABLE

# 6. divmod()
divmod(7,2) # dividendo , divisor

# devuelve (3,1) cociente y resto

# ---------------------------------
# ---------------------------------

# Funciones matemáticas y operadores:

# 1. Suma
resultado_suma = 3 + 5  # resultado_suma es 8

# 2. Resta
resultado_resta = 10 - 4  # resultado_resta es 6

# 3. Multiplicación
resultado_multiplicacion = 2 * 4  # resultado_multiplicacion es 8

# 4. División
resultado_division = 7 / 2  # resultado_division es 3.5

# 5. División entera
resultado_division_entera = 7 // 2  # resultado_division_entera es 3

# 6. Módulo (resto de la división)
resultado_modulo = 10 % 3  # resultado_modulo es 1

# ---------------------------------
# ---------------------------------

# Operadores de comparación:

# 1. Igualdad
x = 5
y = 5
print(x == y)  # Salida: True

# 2. Mayor que
print(5 > 3)  # Salida: True

# 3. Menor que
print(3 < 5)  # Salida: True

# 4. Mayor o igual que
print(5 >= 5)  # Salida: True

# 5. Menor o igual que
print(3 <= 5)  # Salida: True

# 6. No igual que
x = 5
y = 3
print(x != y)  # Salida: True

# ---------------------------------
# ---------------------------------

# Funciones adicionales:

# 1. abs()
x = -10
print(abs(x))  # Salida: 10

# 2. hex()
num = 255
print(hex(num))  # Salida: '0xff'

# 3. pow()
resultado_potencia = pow(2, 3)  # 2 elevado a la potencia de 3
print(resultado_potencia)  # Salida: 8

# 4. round()
num = 3.14159
print(round(num))  # Salida: 3
print(round(num, 2))  # Redondeado a 2 decimales, salida: 3.14

# 5. ord()
caracter_c = 'c'
valor_ascii_c = ord(caracter_c) # sacar el calor ascii de una letra 
print("El valor ASCII de", caracter_c, "es:", valor_ascii_c)

# ---------------------------------
# ---------------------------------

import math # libreria de operaciones matemáticas 

numero = 16
raiz_cuadrada = math.sqrt(numero)

