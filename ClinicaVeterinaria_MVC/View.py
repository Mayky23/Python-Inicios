from Controller import Ficha_nueva, Imprimir_Fichas, get_Ficha_Mascota


def main():

    while True:
        print("__________________________________________")
        print("|     1. Ingresar Nueva Ficha            |")
        print("|     2. Listar todas las Fichas         |")
        print("|     3. Buscar Ficha por num de Socio   |")
        print("__________________________________________")
        opcion = input("Seleccione una opción (1 , 2 o 3): ")
        
        if opcion == '1':
            Ficha_nueva()
        elif opcion == '2':
            Imprimir_Fichas()
        elif opcion == '3':
            get_Ficha_Mascota()
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

        print("_________________________________________")
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        
        if continuar.lower() != 's':
            print("CERRANDO SESIÓN...")
            break

def banner():
    cartel = r"""
      ____ _ _       _            __     __   _            _                  _       
     / ___| (_)_ __ (_) ___ __ _  \ \   / /__| |_ ___ _ __(_)_ __   __ _ _ __(_) __ _ 
    | |   | | | '_ \| |/ __/ _` |  \ \ / / _ \ __/ _ \ '__| | '_ \ / _` | '__| |/ _` |
    | |___| | | | | | | (_| (_| |   \ V /  __/ ||  __/ |  | | | | | (_| | |  | | (_| |
     \____|_|_|_| |_|_|\___\__,_|    \_/ \___|\__\___|_|  |_|_| |_|\__,_|_|  |_|\__,_|
                                                                                                                                  
    """
    print(cartel)

if __name__ == "__main__":

    banner()
    print("______________________________________________________________________________________")
    print()
    main()
