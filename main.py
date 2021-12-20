# Archivos [Python]
# Autor: Ignacio Serrano
# Version: 1.0
import csv, os
def menu():
    print('-------------------------------------')
    print('|¡Bienvenido a Corralon de Materiales')
    print('|Con un N° del 1 al 5 selecciona una opción:')
    print('|(1) ¿Quiere Agregar un Material Nuevo?')
    print('|(2) ¿Quiere Agregar Stock a un Material?')
    print('|(3) ¿Quiere consultar Stock de un material?')
    print('|(4) ¿Quiere Consultar Stock Completo?')
    print('|(5) Salir.')
    print('-------------------------------------')


'''if os.path.exists("archivo.csv") == True:
     # si existe entonces lo abro con "a" en vez de "w"
else:
    # lo abro con "w" para crearlo'''


if __name__ == '__main__':
    p = 0
    while p == 0:
        menu()
        opcion = input()
        if opcion.isnumeric():
            if opcion in range(1,6):
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    p = 1
                    print('Saliendo del programa...\n')
            else:
                print('¡¡¡Seleccion incorrecta!!! Elija un dato valido.\n')
        else:
            print('El valor ingresado debe ser un numero del 1 al 5.\n')