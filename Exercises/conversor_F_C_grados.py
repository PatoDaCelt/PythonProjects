#Programa que pide al usuario una temperatura en Farenheit o en Celsius y la convierte en la contraria

def pasar_C_a_F(temp):
    temp_Fahr = temp * (9/5) + 32
    return temp_Fahr

def pasar_F_a_C(temp):
    temp_Celsius = (temp - 32) * 5/9
    return temp_Celsius

temperatura = float(input("Ingrese el valor de temperatura: "))
opc = input("Escriba C si es Celsius o F si es Fahrenheit: ").lower()

if opc == 'c':
    resultado = pasar_C_a_F(temperatura)
    print(f"La tempratura en Fahrenheit: {resultado}")

if opc == 'f':
    resultado = pasar_F_a_C(temperatura)
    print(f"La tempratura en Celsius: {resultado}")