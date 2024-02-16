# crear una lista 
lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]

# Insertar elementos en un listado
lenguajes.insert(3, "Go") # --> Indice + valor
lenguajes.insert(0, "C")
print(lenguajes)

# Eliminar elementos en un listado
lenguajes.remove("Ruby") # --> Devolver True o False

# Consultar elementos en un listado
print("PHP" in lenguajes)

# Limpiar elementos en un listado
# lenguajes.clear()

# Consultar NUMERO de elementos en un listado
print(len(lenguajes)) # --> Devolver 6