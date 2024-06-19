<<<<<<< HEAD
#1
""" nombres = []

for i in range(3):
    nombre = input(f"Ingrese nombre {i+1}: ")
    nombres.append(nombre) 
       
nombresMasLargo = max(nombres,key=len)
    
print(nombresMasLargo) """

#2
""" 
nombres=[]
apellidos=[]

for i in range(3):
    nombre = input(f"Ingrese nombre {i+1}: ")
    nombres.append(nombre)

    apellido = input(f"Ingrese APELLIDO {i+1}: ")
    apellidos.append(apellido)
    


nombres.sort
apellidos.sort

contador = 0

for i in nombres:
 contador +=1
 print(f"Nombre numero {contador}: {i}")
 
for i in apellidos:
 contador +=1
 print(f"Nombre numero {contador}: {i}")
 """
 #3
 
nombres = []
contador = 0

while True:
    contador += 1
    nombre = input(f"Ingrese nombre {contador}: ")
    nombres.append(nombre)
    print("")
    opcion = input("Desea agregar otro nombre (sí/no): ").lower()  # Corregido
    
    if opcion == "no":
        break


nombresMasCHICO = min(nombres,key=len)

nombres.remove(nombresMasCHICO)

print("La lisssta de nombre es")
for i in nombres:
    
    print(i)
    
OLa = 1
=======
#1
""" nombres = []

for i in range(3):
    nombre = input(f"Ingrese nombre {i+1}: ")
    nombres.append(nombre) 
       
nombresMasLargo = max(nombres,key=len)
    
print(nombresMasLargo) """

#2
""" 
nombres=[]
apellidos=[]

for i in range(3):
    nombre = input(f"Ingrese nombre {i+1}: ")
    nombres.append(nombre)

    apellido = input(f"Ingrese APELLIDO {i+1}: ")
    apellidos.append(apellido)
    


nombres.sort
apellidos.sort

contador = 0

for i in nombres:
 contador +=1
 print(f"Nombre numero {contador}: {i}")
 
for i in apellidos:
 contador +=1
 print(f"Nombre numero {contador}: {i}")
 """
 #3
 
nombres = []
contador = 0

while True:
    contador += 1
    nombre = input(f"Ingrese nombre {contador}: ")
    nombres.append(nombre)
    print("")
    opcion = input("Desea agregar otro nombre (sí/no): ").lower()  # Corregido
    
    if opcion == "no":
        break


nombresMasCHICO = min(nombres,key=len)

nombres.remove(nombresMasCHICO)

print("La lisssta de nombre es")
for i in nombres:
    
    print(i)
    
>>>>>>> 791b4e925a96a99cfa962841c6059e6d8dabd89d
