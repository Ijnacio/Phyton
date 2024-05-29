#Calculadora de promedio:
print("Ingresa 3 numeros para calcular el promedio")
n1 = int(input("Numero uno: "))
n2 = int(input("Numero dos: "))
n3 = int(input("Numero tres: "))
promedio = int((n1 + n2 + n3)/3)
print(f"El promedio es: {promedio}")
#Convertidor de temperaturas:
celcius = float(input("Ingresa temperatura en celsius: "))
farenheit = (celcius * 1.8) + 32
print(f"La temperatura en farenheit es: {farenheit}")
#Caluladore de IMC:
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura en cm: "))
IMC = peso / (altura * altura)
print(f"El IMC es : {round(IMC)}")
#Contador de letras:
palabra = str(input("Ingresa una palabra: "))
print("La cantidad de letra son", len(palabra))
#Calculadora de área y perímetro:
longitud = int(input("Ingresa la longitud del rectangulo: "))
ancho = int(input("Ingresa el Ancho: "))
area = longitud * ancho
perimetro = (2 * longitud) + (2 * ancho)
print(f"El area del rectangulo es: {area} y el perimetro es: {perimetro}")
#Calculadora de volumen:
radio = int(input("Ingresa el radio del cilindro: "))
altura = int(input("Ingresa la altura del cilindro: "))
volumen = 3.14 * (radio **2 ) * altura
print(f"El volumen del cilindro es {volumen}")
#Calculadora de edad:
año = int(input("Ingresa tu año de nacimiento: "))
edad = 2024 - año
print(f"Tu edad es {edad}")
#Calculadora de potencia:
base = int(input("Ingresa numero base: "))
exponente = int(input("Ingrese exponente: "))
solucion = base ** exponente
print(f"el resultado es: {solucion}")