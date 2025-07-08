#Programa que recibe una lista de numeros y devuelve otra lista con los elemetos únicos, es decir, elimina los duplicados.

def eliminar_duplicados(lista_num):
    nueva_lista = set(lista_num)
    return list(nueva_lista)

salida = eliminar_duplicados([1,1,3,4,4,5,2,3,3,8,8,8,8,])
print(salida)