

lista=[
    {
        "categoria": "ACCION",
        "juegos": ["gta","cod","fornite"]
       

    },
    {
        "categoria":"AVENTURA",
        "juegos":["unchurted","prince of persia"]
    },
    {
        "categoria":"DEPORTES",
        "juegos":["fifa20","NBA","MOTO GP"]

    }

]
for categoria in lista:
    print("----------Juegos de:--------------")
    print("",categoria["categoria"])
    
    for juego in categoria["juegos"]:
        print(juego)
