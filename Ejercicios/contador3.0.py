palabra = input("Ingrese una palabra: ").lower()
contador_vocales = {vocal: palabra.count(vocal) for vocal in 'aeiou'}

for vocal, palabra in contador_vocales.items():
    print(f"Cantidad de vocales '{vocal}': {palabra}")