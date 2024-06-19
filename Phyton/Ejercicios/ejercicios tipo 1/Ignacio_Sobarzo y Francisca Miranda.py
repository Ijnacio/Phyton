#Si es mayor de edad

edad = int(input("Ingresa edad: "))

if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")





print("")


#Verifica cuenta
User = str(input("Ingresa Usuario: ")) 
Contraseña = str(input("Ingresa contraseña: "))

if User == "pedro" and Contraseña == "1234":
    print("La cuenta ingresada es correcta")

elif User == "angel" and Contraseña == "a4s1":
        print("La cuenta ingresada es correcta")


else:
     print("La cuenta ingresada es incorrecta")

print("")

#Promedio      


nota1 = float(input("Ingresa nota: "))
nota2 = float(input("Ingresa nota: "))
nota3 = float(input("Ingresa nota: "))

promedio = (nota1 + nota2 + nota3)/3

if promedio >= 4.0:
     print("Aprobaste")
else:
     print("Reprobaste")
print("")

#Que animal vive en agua

puntaje = 0

print("""¿Cual de los siguientes animales vive en el agua?
      Perro
      Cocodrilo
      Conejo
      Tiburon
      """)

animal = str(input("Respuesta: " ))


if animal.lower() == "cocodrilo":
     puntaje += 0.5
     
     print("tu puntaje es: ", puntaje)

elif animal.lower() == "tiburon":
     puntaje += 1.0
     print(f"Tu puntaje es {puntaje}")

else:
     print(f"Tu puntaje es 0")

#3 preguntas con puntaje y nota
puntaje1 = 0     

print("""1.¿Qué personaje de los X-MEN se cura rápidamente?
      Wolverine
      Megamente
      Hulk
      Spider Man
      El Lucas

      """)
respuesta1 = str(input())


if respuesta1.lower() == "wolverine":
     puntaje1 += 1.0

else:
     puntaje1 += 0

print("""y story?
      Buzzlightyear2.Como se llama el astronauta de to
      los picapiedras
      Hulk
      Spider Man
      La pancha

      """)
respuesta2 = str(input())


if respuesta2.lower() == "buzzlightyear":
     puntaje1 += 1.0


else:
     puntaje1 += 0

print("""3.¿Como se llama el burro de Shrek?
      burro
      lucas
      pedro
      caballo
      shrek

      """)

respuesta3 = str(input())


if respuesta3.lower() == "burro":
     puntaje1 = puntaje1 + 1.0

else:
     puntaje1 += 0


##########

if puntaje1 == 1.0:
     nota = 2.7

elif puntaje1 == 0:
     nota = 1.0

elif puntaje1 == 2.0:
    nota = 4.5
    
elif puntaje1 == 3.0:
     nota = 7.0

print(f"Tu puntaje final es: {puntaje1} que equivale a nota {nota}")