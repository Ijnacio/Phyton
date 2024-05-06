"""
El ciclo FOR permite ejecutar una
tarea, un determinado número de
veces (finito por lo general)

"""
#Sintaxis CICLO FOR

#for elemento in secuencia

for i in range(9):
    print("No debo botar la basura", i + 1)

"""
i →Es una variable que es necesaria declarar,
tendrá los valores de la iteración actual
partiendo de cero (perfectamente puede tener
otro nombre).

range()→ función que requiere como argumento el
número de veces que se repetirá el ciclo.


"""

#CICLO WHILE

"""
A diferencia del caso anterior, donde
asignamos un número finito de
repeticiones al ciclo, While permite
ejecutar las fases mientras una
condición se cumpla, cada vez que se
llega a la fase final del ciclo, el
sistema analiza la condición, si se
cumple (True) vuelve a ejecutar cada
una de las fase
"""

#Sintaxis:

#while condicion:
# Código a ejecutar en cada iteración mientras la condición sea verdadera

a = 5
while(a>0):
 print(f"el valor de a es :{a}")
 a = int(input("ingrese un valor: "))
 
 """
 Analicemos la estructura, tiene una
condición de entrada, (a > 0) y
tiene 2 fases:
1) Muestra por pantalla el valor de
“a”

2) Solicita un nuevo valor para “a”
Si ese valor es mayor a 0
(condición) las fases se volverán a
ejecutar, puede ser infinitamente,
dependiendo de los valores que se
ingresen, dado que la condición así
lo dice

 """
 
 