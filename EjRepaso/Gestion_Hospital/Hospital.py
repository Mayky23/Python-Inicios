from EjRepaso.Gestion_Hospital.Pacientes import Paciente

class Hospital: 

    # Lista vacía para almacenar las fichas de pacientes
    BDFichas_Paciente = []
    camas_ocupadas = 0
    camas_total = 100

    @staticmethod
    def set_Ficha_Paciente(ficha):
        # Se agrega la ficha del paciente recibida como parámetro a la lista BDFichas_Paciente
        Hospital.BDFichas_Paciente.append(ficha)
        Hospital.camas_ocupadas += 1

    @staticmethod
    def Ficha_admision(): 
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        genero = input("Ingrese el género del paciente (m / f): ")
        estado = input("Ingrese el estado del paciente: ")
        
        if estado not in Paciente.estado:
            print("Estado de paciente no válido.")
            return
        
        ficha_admision = Paciente(nombre, edad, genero, estado)
        Hospital.set_Ficha_Paciente(ficha_admision)

    @staticmethod
    def salida(): 
        nombre_paciente_alta = input("Ingrese el nombre del paciente: ")
        for paciente in Hospital.BDFichas_Paciente:
            if paciente.nombre == nombre_paciente_alta:
                Hospital.BDFichas_Paciente.remove(paciente)
                Hospital.camas_ocupadas -= 1
                print("El paciente ha sido dado de alta.")
                return
        print("Paciente no encontrado.")

    @staticmethod
    def buscar_paciente():
        print("_________________________________")
        print("|      PACIENTE ENCONTRADO      |")
        print("_________________________________")
        print()

        for paciente in Hospital.BDFichas_Paciente:
            print(f"Nombre de paciente: {paciente.nombre}")
            print(f"Edad: {paciente.edad}")
            print(f"Género: {paciente.genero}")
            print(f"Estado: {paciente.estado}")
        print("_____________________________________") 

    @staticmethod
    def gestion_camas():
        camas_disponibles = Hospital.camas_total - Hospital.camas_ocupadas
        print("Camas totales:", Hospital.camas_total)
        print("----------------------------------")
        print("Camas ocupadas:", Hospital.camas_ocupadas)
        print("Camas libres:", camas_disponibles)

    @classmethod
    def main(cls):
        while True:
            print("____________________________________________")
            print("|  1. Ingresar Nueva Ficha                 |")
            print("|  2. Consultar camas disponibles          |")
            print("|  3. Buscar Ficha por nombre del paciente |")
            print("____________________________________________")
            opcion = input("Seleccione una opción (1 , 2 o 3): ")
            
            if opcion == '1':
                cls.Ficha_admision()
            elif opcion == '2':
                cls.gestion_camas() # Esta función aún no está implementada
            elif opcion == '3':
                cls.buscar_paciente()
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

            continuar = input("¿Desea realizar otra operación? (s/n): ")

            if continuar.lower() == 'n':
                print("CERRANDO SESIÓN...")
                print("_________________________________________")
                break # Termina el bucle while

            elif continuar.lower() != 's':
                print("Entrada inválida. Por favor, ingrese 's' o 'n'.")

if __name__ == "__main__":
    print("______________________________________________________________________________________")
    print()
    Hospital.main()
