word = input("Ingrese el nombre que desea filtrar: ").lower()

with open("names.txt") as file:
    content = file.readlines() #Lee todas las líneas del archivo y las guarda como una lista de strings

#Iterar linea a linea
for line in content:
    #Convertir a minusculas y separar por espacios
    parts = line.strip().lower().split()
    
    #Revisar si la primera palabra es igual a word
    if parts and parts[0] == word:
        print(line.strip()) #Imprime la linea original


#.strip()  Quita espacios al inicio y al final, incluyendo \n
#           'John Smith'
#.lower()  Convierte todo a minúsculas
#           'john smith'
#.split()  Divide el string por espacios → crea una lista de palabras
#           ['john', 'smith']