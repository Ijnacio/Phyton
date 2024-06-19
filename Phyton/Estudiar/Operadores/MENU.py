

#multi y division

while True:
    print("1.Suma\n2.resta\n3.multiplicacion\n4.division\n5.salir")
    opcion = int(input())
    
    if opcion == 1:
        print("Seleccionaste suma")
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        suma = n1 + n2

        print(suma)
    if opcion == 2:
        print("Seleccionaste reesta")
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        resta = n1 - n2
        print(resta)



    if opcion == 3:
        print("Seleccionaste multi")
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        multi = n1 * n2
        print(multi)

    if opcion == 4:
        print("Seleccionaste division")
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        division = n1 / n2
        print(division)

    if opcion == 5:
        print("salir")
        break
