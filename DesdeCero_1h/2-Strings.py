texto = "Hola Mundo"

# Pasar texto a mayuscula
print(texto.upper())

# Pasar texto a minusculas
print(texto.lower())

# Encocntrar un caracter dentro de una cadena -- > devuelve posición 5
print(texto.find("M"))

# Sustituir partes de un string por otras (en caso de ser encontradas)
nuevo_texto = texto.replace("Hola", "Adios")
print(texto, nuevo_texto)

# Comprobar si una cadena está contenida dentro de una variable --> devuelve True / False
print(("Mundo" in texto))