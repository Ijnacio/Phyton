
print("Bienvenido a Donde pepito")
nombre = str(input("¿Cual es su nombre?: "))
edad = int(input("¿Cual es su edad:?: "))
Precio_productos = 0
descuento = 0
descuento1 = 0
descuento_edad = 0




while True:
    print("1. Generar venta")
    print("2. Salir")
    print("Seleciona 1 o 2")
    op= int(input())
    if op == 1:
        
        print("Productos disponibles: ")
        print("1. POROTOS $5.000\n2. Sal $7.000\n3. Jabón 9.000\n4. Papas fritas $ 12.000\n5. Huevos $ 9.000")
        print("¿Que producto desea llevar? Seleccione una opcion numerica")

        while True:
         op2 = int(input())
         if op2 == 1:
            Precio_productos += 5000
         elif op2 ==2:
            Precio_productos += 7000
         elif op2 ==3:
            Precio_productos += 9000
         elif op2 ==4:
            Precio_productos += 12000
         elif op2 ==5:
            Precio_productos += 9000
         print("Desea agregar algun otro producto")
         print("1.si")
         print("2.no")
         
         op3 = int(input())

         if op3 == 1:
            print("1. POROTOS $5.000\n2. Sal $7.000\n3. Jabón 9.000\n4. Papas fritas $ 12.000\n5. Huevos $ 9.000")
            print("¿Que producto desea llevar? Seleccione una opcion numerica")
            continue
         

         
         elif op3 == 2:
            iva = (Precio_productos * 0.19)

            Precio_productos2 = Precio_productos

                
            if edad > 25:
                    descuento_edad = 3990 


            if Precio_productos > 5000:
                descuento = (Precio_productos * 0.10)

            elif Precio_productos >= 10000:
                descuento = (Precio_productos * 0.15)

            elif Precio_productos > 20000:
                descuento = (Precio_productos *0.20)
   
            elif Precio_productos >= 30000:
                descuento = (Precio_productos * 0.25)

            for i in nombre:
          
              if i == "a":
                 descuento1 = (Precio_productos * 0.05)
                 break
   
            total = (Precio_productos2 + iva)
 


            print(f"""***********BOLETA***********
                 Rut de la empresa: 88.696.123-0
                 Tipo de documento: Boleta electrónica
                 Fecha de emisión: 29-04-2024""")
            print(f"printNumero de boleta: 001")
            print("""Giro: Venta de productos envasados
 Dirección: Av. Vicuña Mackenna 4917, 8970117 San Joaquín""")
 
            print(f"Descuento por edad = {descuento_edad}")
            print(f"Descuento por porcentaje de la compra: {descuento}")
            print(F"Descuento por nombre= {descuento1}")
            print(f"Total a pagar: {total}")
            total = (total - descuento1 - descuento - descuento_edad)
            print(f"Toal a pagar despues de los descuentos: {total}")
            print(f"IVA: {iva}")
            break
            


         
    elif op == 2:
       break
