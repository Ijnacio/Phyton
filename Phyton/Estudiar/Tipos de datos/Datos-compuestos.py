#Lista
#Simple Array se  puede modificar las variable

lista = ["Ignacio", "Buenos dias", 19, 65.6,] 
print(lista[2])



#Tupla
#Conjunto de datos que nunca se pueden modificar

tupla = ("Ignacio", "Buenas", True, 777) 
print(tupla[2])

#crendo conjunto (set)
#NO TIENEN ORDEN FIJO y NO SE PUEDEN REPETIR DATOS
#(se accede a dato por dato por un bucle)

conjunto = {"Ignacio", "Buenas", True, 777}

#DICCIONARIO (dict), estrucutura es key : value y se separa por comas menos el ultimo
diccionario = {
 "nombre" : "Ignacio Sobarzo",
 'edad'   : "19 años",
 'altura' : 1.74,
 'esta_emocionado ' : True
# key : "Buenos dias"
}

print(diccionario["nombre"])