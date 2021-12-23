# Archivos [Python]
# Autor: Ignacio Serrano
# Version: 1.0
import csv, os
def menu():
    print('-------------------------------------')
    print('|¡Bienvenido a Corralon de Materiales')
    print('|Con un N° del 1 al 5 selecciona una opción:')
    print('|(1) ¿Agregar un Material Nuevo?')
    print('|(2) ¿Agregar Stock a un Material?')
    print('|(3) ¿Consultar Stock de un material?')
    print('|(4) ¿Consultar Stock Completo?')
    print('|(5) Salir.')
    print('-------------------------------------')


def agrega_material(material, stock):
    if os.path.exists("materiales.csv") == True:
        csvfile = open('materiales.csv', 'a')
        header = ['material', 'stock'] 
        data = csv.DictWriter(csvfile, fieldnames=header)
        fila = {}
        fila['material'] = material
        fila['stock'] = stock
        data.writerow(fila)
        csvfile.close()
    else:
        with open('materiales.csv', 'w', newline='') as csvfile:
            header = ['material', 'stock'] 
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            fila = {}
            fila['material'] = material
            fila['stock'] = stock
            writer.writerow(fila)

        
def buscar_material():
    pass
   
if __name__ == '__main__':
    p = 0
    while p == 0:
        menu()
        opcion = input('Opción: ')
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion in range(1,6):
                if opcion == 1: #Agregar un Material Nuevo?
                    material = input('Ingrese nombre del material: ')
                    stock = input('Ingrese cantidad del material: ')
                    agrega_material(material, stock)
                    #material, stock = ''
                elif opcion == 2: #¿Agregar Stock a un Material?
                    material = input('ingrese material a incrementar: ')
                    buscar_material()
                    #agrega_stock()
                    pass
                elif opcion == 3: #¿Consultar Stock de un material?
                    #consulta_stock_material()
                    pass
                elif opcion == 4: #¿Consultar Stock Completo?
                    #consulta_stock_completo()
                    pass
                elif opcion == 5: #Salir
                    print('Saliendo del programa...\n')
                    p = 1
            else:
                print('¡¡¡Seleccion incorrecta!!! Elija un dato valido.\n')
        else:
            print('El valor ingresado debe ser un numero del 1 al 5.\n')