from FuncionesPDF import *
ListaNombre = []
listaEdades = []
def menu():
 opcion = 1
 while(opcion!=0):
    print("1.pedir datos")
    print("2.imprimir datos")
    print("3.Generar PDF")
    print("4.General QR")
    print("0.salir")
    opcion = int(input("Elige una opcion"))
    if(opcion==1):
        pedirDatos
    elif (opcion==2):
        imprimirDatos()
    elif (opcion==3):
        generarPDF()

def pedirDatos():
    ListaNombre.append(input("ingresa un nombre"))
    ListaNombre.append(input("ingresa un nombre"))
    print("guardado")

def imprimirDatos():
    for i in range(len(ListaNombre)):
        print(f"nombre: {ListaNombre[i]} Edad: {listaEdades[i]}")



