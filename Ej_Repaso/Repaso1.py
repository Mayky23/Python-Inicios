
# Escribir un programa que imprima "Hola, mundo!" en la pantalla.
print("Hola mundo")

# Crear una cadena de caracteres que diga "Hola son las 6 de la tarde" y mostrarla en la pantalla de dos maneras diferentes.
print("Hola son las " + str(6) + " de la tarde")

# Utilizar la función len() para determinar la longitud de una lista o una cadena de caracteres.
lista = [ 1, 2, 3, 4, 5]
print(len(lista))

# Solicitar al usuario que introduzca su nombre utilizando la función input() y luego saludarlo.
nombre = input("Introduce tu nombre: ")
print("Hola: ", nombre)

# Utilizar un bucle for y la función range() para imprimir los números del 0 al 4 en la pantalla.
for i in range (5):
    print(i)

# Determinar el tipo de una variable utilizando la función type().
num = 10
print(type(num))

# Utilizar la función divmod() para obtener el cociente y el resto de la división de 7 entre 2.
divmod(7,2)

# Realizar operaciones matemáticas básicas como suma, resta, multiplicación, división, división entera y módulo.
r_suma = 5 + 5
r_resta = 5 - 3
r_multiplicacion = 5 * 5
r_div = 7 / 2
r_modulo = 10 % 3

print("resultados: ", r_suma, r_resta, r_multiplicacion, r_div, r_modulo)

# Utilizar operadores de comparación para comparar valores y determinar si son iguales, mayores, menores, etc.
a = 5
b = 5

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)

# Utilizar la función abs() para obtener el valor absoluto de un número.
x = -20
print(abs(x))

# Convertir un número en su representación hexadecimal utilizando la función hex().
w = 50
print(hex(w))

# Elevar un número a una potencia utilizando la función pow().
r = 25
rb = 50
print(pow(r, rb))

# Redondear un número utilizando la función round() con y sin especificar el número de decimales.
numerito = 5.2023423532
print(round(numerito))
print(round(numerito, 3))

# Obtener el valor ASCII de un carácter utilizando la función ord().
caracter_ascii = 'a'
print(ord(caracter_ascii))

# Importar la biblioteca math y utilizar la función sqrt() para calcular la raíz cuadrada de un número.
import math

numero2 = 50
print(math.sqrt(numero2))