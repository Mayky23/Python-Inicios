# datos del paciente, como nombre, edad, género y condición médica

class Paciente:
# Atributos de paciente.
    """
    estado = ["Ingresado", 
            "En observación", 
            "En tratamiento", 
            "Esperando atención", 
            "En cirugía",
            "En consulta",
            "Dado de alta"]
    """

    def __init__(self, nombre, edad, genero, estado):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.estado = estado