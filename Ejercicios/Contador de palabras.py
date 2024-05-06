
palabra=str(input("Ingresa una palabra: ")).lower()

contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0


for i in palabra:

    if i == "a":
        contadorA += 1
    elif i == "e":
        contadorE += 1
    elif i == "i":
        contadorI += 1   
    elif i == "o":
        contadorO += 1
    elif i == "u":
        contadorU += 1
        
print(f"Hay un total de {contadorA} a en la palabra")


print(f"Hay un total de {contadorE} E en la palabra")

        
print(f"Hay un total de {contadorI} I en la palabra")

        
print(f"Hay un total de {contadorO} O en la palabra")

    
print(f"Hay un total de {contadorU} U en la palabra")
