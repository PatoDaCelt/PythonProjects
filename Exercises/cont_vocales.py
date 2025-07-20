#Funcion que cuenta cuantas vocales hay en una palabra
def contar_vocales(palabra):
    vocales = ['a','e','i','o','u']
    cont = 0
    for letra in palabra:
        if letra in vocales:
            cont += 1
    return cont

palabra = input("Ingrese una palabra: ").lower()
conteo = contar_vocales(palabra)

print(f"La palabra tiene {conteo} vocales.")