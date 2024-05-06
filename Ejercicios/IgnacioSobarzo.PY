nombre = str(input("Ingresa tu nombre: ")).lower()

edad = int(input("Ingresa tu edad: "))

descuento = 0

if nombre == "agustin":
    descuento += 10

elif nombre == "matias":
    descuento += 40

elif nombre == "tomas":
    descuento -= 10

elif nombre == "mario":
    descuento += 10

elif nombre == "miguel":
    descuento -= 15

elif nombre == "escobar":
    descuento += 20
    
elif nombre == "mateo":
    descuento -= 30

elif nombre == "carlos":
    descuento += 40

elif nombre == "sebastian":
    descuento += 10

#DESCCUENTO EDAD ECXACTA

if edad == 10:
    descuento+= 2
elif edad == 20:
    descuento += 6
elif edad == 30:
    descuento -= 7
elif edad == 40:
    descuento -= 8
elif edad == 50:
    descuento += 12
    
    

# Descuentos basados en la edad
if 1 <= edad <= 10:
    descuento += 15
    
elif 11 <= edad <= 20:
    descuento -= 25
    
elif 21 <= edad <= 30:
    descuento += 35
    
elif 31 <= edad <= 40:
    descuento += 45
    
elif 41 <= edad <= 70:
    descuento -= 55
    

# Condiciones especiales combinando nombre y edad

if nombre == "matias" and edad == 10:
    descuento -= 3
    
elif nombre == "matias" and edad == 15:
    descuento += 6
    
elif nombre == "matias" and edad == 35:
    descuento += 7

if nombre == "mario" and 20 <= edad <= 60:
    descuento += 40

elif nombre == "miguel" and 10 < edad < 30:
    descuento += 35
    
    if edad == 25:
        descuento += 5

if nombre == "sebastian" and edad != 40 and edad != 43 and edad != 12:
    descuento += 7

elif nombre in "tomas" "joaquin" "benjamin" and edad % 2 == 0:
    descuento += 20

if nombre == "escobar" and edad % 2 == 0:
    descuento += 10

if nombre in "mateo" or nombre in "esteban" and edad % 2 != 0:
    descuento -= 5

# Condiciones extras o aleatorias
if 1 <= len(nombre) <= 5:
    descuento += 20

print(f"Tu descuento es de {descuento}%")