#SUMAR TODOS LOS NÚMEROS EN UN RANGO DEFINIDO POR EL USUARIO

#Pedir al usuario que ingrese el valor inicial y el valor final
#Función que recorra cada número desde el principio hasta el final y calcule la sume total

num_start = int(input("Ingresa el rango de inicio: "))
num_end = int(input("Ingresa el rango de fin "))

def sum_all(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

print(sum_all(num_start, num_end))