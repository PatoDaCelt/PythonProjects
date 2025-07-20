#Juego del Hangman básico

#El programa elige una palabra secreta y permite al usuario adivinar una letra a la vez

#Tras cada intento, mostrara su progreso revelando las letras correctas y dejando guiones bajos (_) para las letras que aun no adivina

#El usuario tendrá un numero limitado de intentos incorrectos. Si acierta todas las letras antes de quedarse sin intentos, gana, de lo contrario, pierde y se muestra la palabra.

palabra_secreta = "python"
letras_adivinadas = []
intentos_max = 6
num_intentos = 0

while True:
    #Muestra progreso
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += '_'
    print(progreso)
    
    #Verifica si gana
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("\r¡Felicidades! Adivinaste la palabra")
        break
    
    #Pedir una letra al usuario
    intento = input("Ingresa una letra: ").lower()
    
    #SI ya se uso esa letra
    if intento in letras_adivinadas:
        print("ESA LETRA YA LA USASTE. PRUEBA OTRA.")
        continue
    
    #Si es más de una letra o no es una letra
    if len(intento) != 1 or not intento.isalpha():
          print("PORFAVOR, INGRESA SOLO UNA LETRA VÁLIDA.")
    
    #Registra la letra como letra adivinada
    letras_adivinadas.append(intento)
    
    #Verifica si la letra pertenece a la palabra secreta
    if intento in palabra_secreta:
        print("✅\n")
    else:
        num_intentos += 1
        print("❌, intentos:", intentos_max - num_intentos, "\n")
    
    #Verifica si perdio
    if num_intentos >= intentos_max:
        print("TE QUEDASTE SIN INTENTOS, HAS PERDIDO. \n La palabra era: ", palabra_secreta)
        break