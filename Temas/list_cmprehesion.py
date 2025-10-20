#Obtener cuadrados de los números del 1 al 10
def cuadrados(lista):
    new_list = [num**2 for num in lista]
    return new_list

#Extraer solo los numeros pares de la lista
def solo_pares(lista):
    new_list = [num for num in lista if num%2 == 0]
    return new_list

#print(solo_pares([1,2,3,4,5,6,7,8,9,10]))

#Filtrar palabras con más de 4 letras
def word_mas_5_letras(list):
    new_list = [palabra for palabra in list if len(palabra) > 4 ]
    return new_list
# lista = ["sol", "montaña", "cielo", "universo", "mar"]

#Convertir una lista de strings a mayusculas
def hacer_mayusculas(list):
    new_list = [palabra.upper() for palabra in list]
    return new_list
# nombres = ["ana", "luis", "carlos"]

#Eliminar valores vacios de una lista
def quitar_vacios(list):
    new_list = [palabra for palabra in list if len(palabra) > 1]
    return new_list
# datos = ["Python", "", "AI", "", "Data"]

#Lista nueva con el producto de cada elemento de lista1 por cada elemento de lista2
def prod_list():
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    new_list = [num1 * num2 for num1 in lista1 for num2 in lista2]
    return new_list

#Filtrar solo los números enteros de una lista mixta
def filtrar_enteros():
    mezcla = [1, 'a', 2.5, 3, 'b', 4]
    new_list = [dato for dato in mezcla if isinstance(dato, str)]
    return new_list

#Crear una lista con los números del 1 al 100 que sean divisibles por 3 o 5
def num_1_a_100_divisibles_3_o_5():
    list = []
    for i in range(1,101):
        list.append(i)
    new_list = [num for num in list if (num%3 == 0 or num%5 == 0)]
    return new_list


def obtener_vocales():
    texto = "List comprehensions son geniales"
    vocales = ['a','e','i','o','u']
    new_list = [letra1 for letra1 in texto for letra2 in vocales if letra1 == letra2]
    return new_list
    

print(obtener_vocales())