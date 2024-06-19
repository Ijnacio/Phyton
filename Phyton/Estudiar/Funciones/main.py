import  funciones as fcn

menu = ("Sumar","Restar","Dividir", "Multiplicar","Salir")
contador = 0
while True:
    numeroUno = int(input("Ingrese el primer número: "))
    numeroDos = int(input("Ingrese el segundo número: "))

    for i in menu:
        contador+=1
        print(f"[{contador}] - {i}")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print(fcn.sumar(numeroUno,numeroDos))
    if opcion == 2:
        print("Restar")
    if opcion == 3:
        print("Dividir")
    if opcion == 4:
        print("Multiplicar")
    if opcion == 5:
        break

