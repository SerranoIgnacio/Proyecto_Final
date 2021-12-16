# Archivos [Python]
# Autor: Ignacio Serrano
# Version: 1.0
import csv, os
def menu():
    print('-------------------------------------')
    print('|¡Bienvenido a Corralon de Materiales')
    print('|Con un N° del 1 al 5 selecciona una opción:')
    print('|(1) ¿Quiere consultar Stock de un material?')
    print('|(2) ¿Quiere Consultar Stock Completo?')
    print('|(3) ¿Quiere Agregar un Material Nuevo?')
    print('|(4) ¿Quiere Agregar Stock a un Material?')
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
        opcion = int(input())
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
    