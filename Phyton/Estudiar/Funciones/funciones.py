""" def suma():
    print(1+1)
    nombre = "Pedro"
    print(nombre)

suma() """

""" def suma(numUno:int,numDos:int):
    
    print(numUno + numDos)

suma(128,128)
suma(256,256) """

""" def suma():
    return 100+100

resultadoSuma = suma()

print(resultadoSuma + 50) """

""" def suma(n1:int, n2:int) -> int:
    return n1 + n2
 
suma(400,100) """



def sumar(n1:int,n2:int) -> int:
    return n1 + n2

def restar(n1:int, n2:int) -> int:
    return n1 - n2

def dividir(n1:int, n2:int) -> float:
    return n1 / n2

def multiplicar(n1:int, n2:int) -> int:
    return n1 * n2