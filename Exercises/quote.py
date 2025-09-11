#Programa que guarda una cita ingresada por el usuario en un txt y luego la lee y la muestra como salida.

quote = input("¿Cual es tu cita favorita? ")

with open("quote.txt", 'a+', encoding="utf-8") as file:
    content = file.write(quote)
    file.seek(0)
    content = file.read()

print(f"Tu cita favorita es: -{content}-") 