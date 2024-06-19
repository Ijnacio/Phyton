total_pasajes = int(input("¿Cuántos pasajes deseas vender?: "))
total_ingresos = 0

for i in range(total_pasajes):
    try:
        precio_pasaje = float(input(f"Ingrese el precio del pasaje {i + 1}: "))
        total_ingresos += precio_pasaje
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

print(f"El monto total obtenido por la venta de {total_pasajes} pasajes es: {total_ingresos}")
