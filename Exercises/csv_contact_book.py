#Libro de contactos que guarda Nombre, numero y correo en un CSV.
import csv
import os
import pandas as pd

while True:

    opc = input("Agregar contacto: a \n Ver contactos: s \n").lower()

    if opc == "a":
        file_exists = os.path.isfile("contacts.csv")

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        with open("contacts.csv", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # Si el archivo no existe, escribimos los encabezados
            if not file_exists:
                writer.writerow(["Name", "Phone", "Email"])
            
            # Escribimos los datos del nuevo contacto
            writer.writerow([name, phone, email])

        print("Contact saved...\n")

    elif opc == "s":
        tabla = pd.read_csv("contacts.csv")
        print(tabla)
        print("\n")
        
