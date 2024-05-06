palabra = input("Ingrese una palabra: ")
contador_vocales = {vocal: palabra.lower().count(vocal) for vocal in 'aeiou'}

for vocal, palabra in contador_vocales.items():
    print(f"Cantidad de vocales '{vocal}': {palabra}")