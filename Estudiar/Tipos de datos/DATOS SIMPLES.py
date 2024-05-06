#DATOS SIMPLES (son 4 los principales)

#1.String (texto)

#el string es texto y se puede escribir de dos formas
#1) "hola", 2) 'hola'

#tambien se puen usar 3 comillas para poder hacer varias lineas de texto

"""OLA
NOMBRE: iGNACIO
RUT: 219382323
ola como etas ignacio"""

#2.INT (numero entero) ej ...,

from sre_constants import IN


-2, -1, 0, 1, 3, 4, 5, 6,...

#3.Float (numero decimales) ej 
2.34, 0.5, 3.14

#4. Booleanos (Verdadero o Falso)

True, False

#VARIABLES

#Que es una variable? 
#En palabras sencillas, una variable es un contenedor que se utiliza para almacenar información en un programa de computadora. 
#Puedes pensar en una variable como una caja etiquetada en la que puedes guardar diferentes tipos de datos 
#como números, texto o valores booleanos."""

#INT
A = 1
B = 3

C = A * B 

#String
Nombre = "renato"

#Bool
elvalores = True

#Float
numero = 3.24




#Concatenacion y F string
#Concatenacion es cuando se unen dos strings (cadenas) $recordar que cada caracter cuenta hasta el " "
#Fstring es cuando agarras el valor de tu variable y la conviertes en texto.
numero1 = 19
nombre  = "renato"
bienvenida = f"Hola {nombre} Como estas? tu edad es {numero1} cierto?"


del nombre #El del permite borrar una variable.


#Operadores de pertenencia e Identidad

#pertenencia
print("ola" in bienvenida) #ola esta en bienvenida - Si las letras "ola" se encuentran en la variable bienvenida arrojara True y si no esta False.
#identidad
print("Hola" not in bienvenida) #hola no esta bienvenida - Su las letras "Hola" no esta en la variable bienvenida arrojara False y si no True.

#Operadores Logicos

"""
+=
-=
<, <=
>, >=
* (multiplicar)
/ (dividir)

"""

#Como imprimir?
#Para imprimir se necesita escribir print("Ola", 3, 3,15, True,)
#Para pedir que ingrese datos a una variable es
#llamaremos una variable NOMBRE

NOMBRE = input("Ingrese nombre: ") #imprimira Ingrese nombre: (ACA ingresaremos el nombre)

#Si usamos esto:

print("Hola ", NOMBRE) #imprimira Hola (ACA EN NOMBRE INGRESADO)

#Tambien podemos hacerlo de esta manera

print("Ingresa nombre: ")
NOMBRE1 = input()

#esto imprimira Ingresa nombre    
#(ACA INGRESAREMOS EL NOMBRE)

#Son dos formas epro hacen lo mismo

print("Hola ", NOMBRE1) #imprimira Hola (ACA EN NOMBRE INGRESADO)

#se pueden sumar numeros sin declarar variables
print(2 + 2)

print("El numero 2 + 2 es: ", 2 + 2 )



# \t signfica tabulear y te saltas un espacio hacia la derecha
# \n significa te saltas una linea hhacia abajo









