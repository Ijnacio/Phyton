# Variables y Tipos de Datos
variable_entera = 42 
variable_decimal = 3.14
variable_texto = "Hola, mundo!"
variable_booleana = True

# Operadores
resultado_suma = variable_entera + variable_decimal
comparacion = (variable_entera > variable_decimal)

# Entrada y Salida
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre_usuario + "! Este es tu primer programa en Python.")

# Estructuras de Control de decisiones
if variable_booleana:
    print("La variable booleana es verdadera.")
elif resultado_suma < 10:
    print("La suma es menor que 10.")
else:
    print("Ninguna de las condiciones anteriores se cumple.")

# Funciones
def saludar(nombre):
    return "¡Hola, " + nombre + "!"

mensaje_saludo = saludar("Estudiante")

# Manejo de Errores
try:
    resultado_division = 0 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")
finally:
    print("Bloque 'finally': Este código se ejecuta siempre, haya o no haya errores.")

# Trabajo con Archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("¡Hola desde un archivo!")

# Módulos y Bibliotecas
import math
raiz_cuadrada = math.sqrt(16)

# Programación Orientada a Objetos
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo
        
    def mostrar_atributo(self):
        print("El valor del atributo es:", self.atributo)

# Manejo de Cadenas (Strings)
longitud_cadena = len("Python")
mayusculas = "hola".upper()
minusculas = "HOLA".lower()
reemplazo = "python es divertido".replace("divertido", "increíble")
