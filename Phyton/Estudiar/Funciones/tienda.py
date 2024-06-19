import json






def agregarCliente(nombre:str,credito:int):
    with open("new/compras.json",mode="r") as archivoJson:
        leerJson = json.load(archivoJson)
        cliente = {
        "id":len(leerJson["clientes"])+1,
        "nombre":nombre,
        "credito":credito
        }
        leerJson["clientes"].append(cliente)


    with open("new/compras.json",mode="w") as archivoJson:
        json.dump(leerJson,archivoJson,indent=4)


""" nombre = input("Ingrese el nombre del cliente ")
credito = int(input("Ingrese el credito del cliente "))

agregarCliente(nombre,credito) """



def editarCliente(id:int,nombre:str,credito:int):
    with open("new/compras.json",mode="r") as archivoJson:
        leerJson = json.load(archivoJson)

        contador = 0
        for i in leerJson["clientes"]:
            if i["id"] == id:
                print("Encontre!!",contador)
                break
            contador+=1

        #print(leerJson["clientes"][contador])
        leerJson["clientes"][contador]["nombre"] = nombre
        leerJson["clientes"][contador]["credito"] = credito

    with open("new/compras.json",mode="w") as archivoJson:
        json.dump(leerJson,archivoJson,indent=4)


        
editarCliente(4,"Felipe",100)