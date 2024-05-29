miPrimeraLista = ['Rojo','Amarillo',10,20,30,30]

print(miPrimeraLista[2])

for i in miPrimeraLista:
    print(i, end = ' ')


""" """ """ miPrimeraLista.append(100)
miPrimeraLista.insert(1,500)
miPrimeraLista.remove('Rojo')
miPrimeraLista.pop(0)
#miPrimeraLista.clear()


#print(miPrimeraLista.count(30))
miPrimeraLista.reverse()
#print(miPrimeraLista) """

""" listaUno = [1,2,3]
listaDos = [4,5,6]

for i in listaUno:
    listaDos.append(i)

listaDos.sort(reverse=False)

print(listaDos)

 """
""" 

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print(matriz[3][1])

for i in matriz:
    for j in i:
        print(j)
 """

"""
arreglo_3D = [
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [7, 8, 9],
        [10, 11, 12],
    ],
    [
        [13, 14, 15],
        [16, 17, 18],
    ]
]

print(arreglo_3D[1][1][1])


for i in arreglo_3D:
    for j in i:
        for k in j:
            print(k, end = ' ')



listaNombre = []

for i in range(3):
    nombre = input("Ingrese un nombre: ")
    listaNombre.append(nombre)

print(max(listaNombre))
     """
