temperatura = float(input("Ingrese una temperatura a convertir:"))

opcion = input("Es Celsius (c) o Fahrenheit (f) :")

if opcion == "C" or opcion == "c" :
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)

elif opcion == "F" or opcion == "f" :
    celsius = (temperatura - 32) * 5/9
    print(celsius)

else:
    print("Inserte un valor válido...")