<<<<<<< HEAD
"""
Deberás construir un programa que está diseñado para ayudar en la venta
de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
cada pasaje por separado. Si ingresas un valor que no es un número, te
indica que necesitas proporcionar un valor numérico válido. Al final, muestra
el monto total que se ha obtenido por la venta de todos los pasajes
 Solicita al usuario la cantidad de pasajes a vender.
 Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
 Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
acumula en la variable totalIngresos.
 Si el usuario ingresa un valor no numérico para el precio del pasaje,
el programa muestra un mensaje y sale del bucle usando break.
 Finalmente, se imprime el total de ingresos por la venta de pasajes
"""

cantidad_pasajes = int(input("Cuantos pasajes desea vender: "))
total_ingresos = 0

for i in range(cantidad_pasajes):
    try: 
        precio_pasaje = int(input(f"Ingrese el precio del pasaje Nmr {i+1}: "))
        total_ingresos += precio_pasaje
       
    except ValueError:
        print("ERROR, ingresasate una letra")
        
        break
    

print(f"El monto total obtenido por la venta de {i} pasajes es: {total_ingresos}")


total_pasajes = int(input("¿Cuántos pasajes deseas vender?: "))
total_ingresos = 0

for i in range(total_pasajes):
    while True:
        try:
            precio_pasaje = int(input(f"Ingrese el precio del pasaje {i + 1}: "))
            total_ingresos += precio_pasaje
            break
        
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
            
print(f"El monto total obtenido por la venta de {total_pasajes} pasajes es: {total_ingresos}")
=======
"""
Deberás construir un programa que está diseñado para ayudar en la venta
de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
cada pasaje por separado. Si ingresas un valor que no es un número, te
indica que necesitas proporcionar un valor numérico válido. Al final, muestra
el monto total que se ha obtenido por la venta de todos los pasajes
 Solicita al usuario la cantidad de pasajes a vender.
 Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
 Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
acumula en la variable totalIngresos.
 Si el usuario ingresa un valor no numérico para el precio del pasaje,
el programa muestra un mensaje y sale del bucle usando break.
 Finalmente, se imprime el total de ingresos por la venta de pasajes
"""

cantidad_pasajes = int(input("Cuantos pasajes desea vender: "))
total_ingresos = 0

for i in range(cantidad_pasajes):
    try: 
        precio_pasaje = int(input(f"Ingrese el precio del pasaje Nmr {i+1}: "))
        total_ingresos += precio_pasaje
       
    except ValueError:
        print("ERROR, ingresasate una letra")
        
        break
    

print(f"El monto total obtenido por la venta de {i} pasajes es: {total_ingresos}")


total_pasajes = int(input("¿Cuántos pasajes deseas vender?: "))
total_ingresos = 0

for i in range(total_pasajes):
    while True:
        try:
            precio_pasaje = int(input(f"Ingrese el precio del pasaje {i + 1}: "))
            total_ingresos += precio_pasaje
            break
        
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
            
print(f"El monto total obtenido por la venta de {total_pasajes} pasajes es: {total_ingresos}")
>>>>>>> 791b4e925a96a99cfa962841c6059e6d8dabd89d
