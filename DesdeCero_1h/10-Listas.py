# crear una lista 
lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]

# Imprimir una lista
print(lenguajes)

# Imprimir una posición concreta de la lista
print(lenguajes [1]) # --> Ruby

# Cambiar elemento concreto de la lista
lenguajes[1] = "Go"
print(lenguajes [1]) # --> Go

# Podemos usar índices negativos : Se compieza desde el final de la lista
print(lenguajes [-1]) # --> Java

# Podemos seleccionar un rango de elementos de la lista
print(lenguajes [1:3]) # --> Donde Inicia y termina
print(lenguajes [:3]) # --> Se toma por defecto el primer elemento
print(lenguajes [1:]) # --> Se recorren hasta el ultimo elemento