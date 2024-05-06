#EJERCICIO  1


liviano = 1000
normal = 2000
total_liviano = 0
total_normal = 0
contador_liviano = 0
contador_normal = 0

bultos = int(input("Ingresa la cantidad de bultos: "))

"""
for i in range(bultos):
  try:    
   pesobulto = int(input(f"Ingrese el peso del bulto nro {i+1}: "))

  except ValueError:
     print("ERROR")
     print("error debe ingresar un NUMERO entre 1 y 10") 
     continue
 
  if 1 <= pesobulto <= 5:
     total_liviano += liviano
     contador_liviano += 1
    
  elif 5 <= pesobulto <= 10:
    total_normal += normal
    contador_normal += 1
    
  else:
     print("EL PESO DEBE SER ENTRE 1 Y 10  ")
     
     
print(f"Total a pagar por bultos livianos: {total_liviano} \nTotal a pagar por bultos normales: {total_normal} ")
print(f"Cantidad de bultos livianos: {contador_liviano} \nCantidad de bultos normales: {contador_normal}")

"""
x = 1

while bultos >= x:
 try:    
   pesobulto = int(input(f"Ingrese el peso del bulto nro {x}: "))

 except ValueError:
     print("ERROR")
     print("error debe ingresar un NUMERO entre 1 y 10") 
     continue
 
 if 1 <= pesobulto <= 5:
     total_liviano += liviano
     contador_liviano += 1
    
 elif 5 <= pesobulto <= 10:
    total_normal += normal
    contador_normal += 1
    
 else:
     print("EL PESO DEBE SER ENTRE 1 Y 10  ")
 x+=1    
     
print(f"Total a pagar por bultos livianos: {total_liviano} \nTotal a pagar por bultos normales: {total_normal} ")
print(f"Cantidad de bultos livianos: {contador_liviano} \nCantidad de bultos normales: {contador_normal}")

        
        
        
    
