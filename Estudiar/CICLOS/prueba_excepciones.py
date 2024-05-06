from sys import exception


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
	
def divide(num1,num2):		
	
 try:
     return num1/num2
 except ZeroDivisionError:
    print("NO se puede dividir entre 0")
    return "operacion erronea"

op1=(int(input("Introduce el primer nimero: ")))

op2=(int(input("Introduce el segundo nimero: ")))		
	
operacion=input("Introduce la operaciin a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operaciin no contemplada")


print("Operaciin ejecutada. Continuaciin de ejecicii del programa ")

"""
TIPOS DE ERRORES MÁS COMUNES:

1. Divisiones por cero (10/0). -> ZeroDivisionError

2. Tipos de datos incorrectos (Aparece cuando intentas concatenar una cadena con un
número. ) -> TypeError

3. Error de valores (Se genera cuando hay un problema con el tipo o valor de los
datos que estás manipulando, como convertir una cadena no numérica a un número )
- > ValueError

4. Archivos no encontrados (Dar ubicaciones de archivo no existentes) ->
FileNotFoundError

5. Error de sintaxis (Se genera cuando hay un error de sintaxis en tu código ) ->
SyntaxError


"""