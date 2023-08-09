from FuncionesPDF import *
from datosEstaticos import *
ListaClientes = []

def menu():
    opcion = 1
    while opcion != 0:
        print("1. Lista de productos")
        print("2. Promociones")
        print("3. Elegir productos para comprar")
        print("4. Imprimir lista de proveedores locales")
        print("5. Imprimir lista de proveedores externos")
        print("6. Imprimir datos")
        print("0. Salir")
        
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            ListarProductos() 
         
        elif opcion == 2:
            
            pass
        elif opcion == 3:
            Compras()
        elif opcion == 4:
           
            pass
        elif opcion == 5:
           
            pass
        elif opcion == 6:
            imprimirDatos()


def ListarProductos(): 
    print("|producto|","|precio|")
    for i in range (len(listaProductosGenerales)):
        print(f"{i+1} {listaProductosGenerales[i]} {listaPrecios[i]}")
    elegido = int(input("que productos quieres comprar?"))
    print(f"Elegiste { listaProductosGenerales[elegido-1]} debes pagar {listaPrecios[elegido-1]}")


def Compras():
    Seleccionado = []
    while True:
        select = int(input("Elige un producto (0 para terminar): "))
        
        if select == 0:
            break
        
        if select < 1 or select > len(listaProductosGenerales):
            print("Opción inválida o producto no disponible. Por favor, elija un producto válido.")
        else:
            Seleccionado.append((listaProductosGenerales[select - 1], listaProductosGenerales[select - 1], listaPrecios[select - 1]))
            print("Producto agregado")
    
    return Seleccionado

def imprimirDatos():
    print('{:<29} {:<20}'.format("| Nombre |", "| Correo electrónico |"))
    for i in range(len(ListaClientes)):
        print('{:<29} {:<20}'.format(ListaClientes[i][0], ListaClientes[i][1]))

menu()
   

        
    
        
    

        




  
 
