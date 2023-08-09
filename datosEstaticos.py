listaProductosGenerales = ["Pepsi ",
                           "Sabritas",
                           "Cafe",
                           "Sal","Huevo","Leche","Nuecez", "Semillas","papel higienico","Mazapan","gansito","Pan dulce",
                           "Cerveza","Tequila","vodka","Suero","Suero","Garrafon de agua","Shampoo para ropa","Jarrito","Pasta de dientes","Fanta"
                           "Galletas", "coca cola", "salsa picante", "Te", "mantequilla", "Mayonesa" ,"Chiles",
                            "jamón" , "atun enlatado ", "agua embotellada" "mermelada", "Salvo", "Ariel", "Ace", "Atole", "Chile piquín" 
                            "Gelatinas en polvo/Grenetina", "Atún en agua/aceite" , "Agua mineral" , "Algodón", "Toallas Higienicas ","fritos", "Rufles", 
                            "chiles","45 Paletas", "Cigarros","Nescafe", "salchichas"           ]

listaPrecios = [
    15.0, 10.0, 25.0, 5.0, 20.0, 30.0, 40.0, 12.0, 8.0, 18.0, 15.0, 22.0,
    150.0, 200.0, 50.0, 25.0, 10.0, 8.0, 30.0, 18.0, 15.0, 12.0, 20.0, 10.0,
    35.0, 15.0, 25.0, 7.0, 40.0, 28.0, 10.0, 15.0, 10.0, 40.0, 30.0, 5.0,
    10.0, 20.0, 18.0, 5.0,8.0,8.0, 18.0, 15.0, 22.0,28.0, 10.0, 15.0, 10.0, 40.0,
    150.0, 200.0
]


def ListarProductos(): 
    for i in range (len(listaProductosGenerales)):
        print(f"{listaProductosGenerales[i]}-{listaPrecios[i]}")

        ListarProductos()

        elegido = int(input("que productos quieres comprar?"))
        print(f"Elegiste { listaProductosGenerales[elegido-1]} debes pagar {listaPrecios[elegido-1]}")












