try:
    # Pedir datos al usuario
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))

    # Validar que la altura no sea cero
    if altura == 0:
        print("Error: La altura ingresada no puede ser cero.")
        
    else:
        # Calcular el IMC
        imc = peso / (altura ** 2)
        
        # Mostrar el resultado con 2 decimales
        print(f"Tu IMC es: {imc:.2f}")

        # Clasificar según el IMC
        if imc < 18.5:
            print("Estado: Bajo Peso")
        elif 18.5 <= imc < 24.9:
            print("Estado: Peso Normal")
        elif 25 <= imc < 29.9:
            print("Estado: Sobrepeso")
        else:
            print("Estado: Obesidad")

except ValueError:
    print("Error: Por favor, introduce solo números válidos.")