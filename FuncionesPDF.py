from reportlab.pdfgen import canvas
ruta = "C:/Users/monse/OneDrive/Escritorio/principal/prueba funciones/"
nombreArchivo = ruta + "reporte.pdf"

def generarPDF(listaNombres, ListaEdades):
    c = canvas.Canvas(nombreArchivo)

    xInicial = 200
    yInicial = 700

    c.setFont('Helvetica', 20)
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial + 120, yInicial,"nombre")

    for i in range(len(listaNombres)):
        c.setFont('Helvetica', 18)
        yInicial = yInicial - 20
        c.drawString(xInicial ,yInicial ,ListaEdades[i])
        c.drawString(xInicial +120, yInicial,listaNombres[i])

    c.save()
    print("reporte generado----")

