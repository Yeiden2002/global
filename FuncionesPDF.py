from reportlab.pdfgen import canvas
from FuncionesQR import *
ruta = "C:/Users/monse/OneDrive/Escritorio/principal/prueba funciones/"
nombreArchivo = ruta + "reporte.pdf"
nombreQR = ruta  + "miQR.png"
def generarPDF(listaNombres, ListaEdades):
    generarQR(nombreQR, "hola desde funcion")
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700

    c.setFont('Helvetica', 20)
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial + 120, yInicial,"nombre")
    c.drawImage(nombreQR,200,400,100,100)
    for i in range(len(listaNombres)):
        c.setFont('Helvetica', 18)
        yInicial = yInicial - 20
        c.drawString(xInicial ,yInicial ,str(ListaEdades[i]))
        c.drawString(xInicial +120, yInicial,listaNombres[i])

    c.save()
    print("reporte generado----")

