"""
Crear un programa que solicite al usuario ingresar un número entero positivo. 
Luego, el programa deberá calcular la raíz cuadrada de dicho número y redondear
el resultado a dos decimales. Después, el programa imprimirá en la pantalla el 
resultado de la raíz cuadrada junto con su valor redondeado, utilizando el 
formato 'La raíz cuadrada de [número] es [resultado_raiz] y 
redondeado es [resultado_redondeado]'. Además, el programa verificará si 
el número ingresado es mayor que 10 y si es así, imprimirá 'El número ingresado 
es mayor que 10', de lo contrario imprimirá 'El número ingresado es igual o menor que 10'."

Este ejercicio involucra solicitar entrada al usuario, realizar cálculos matemáticos,
utilizar estructuras condicionales (if), formatear la salida para imprimir en pantalla,
y trabajar con valores enteros, la función input(), operaciones matemáticas básicas, l
a biblioteca math para calcular la raíz cuadrada y la función round() para redondear números.

"""
import math

numUser = int(input("Inserte un número entero: "))


if numUser > 10 :
    print("\nEl número ingresado es mayor que 10")

else:
    print("\nEl número ingresado es igual o menor que 10")

r_cuadrada = math.sqrt(abs(numUser))

num_redondeo = round(r_cuadrada, 2)

print("\nLa raíz cuadrada de", numUser, "es", num_redondeo)