nombre = "Johnier"
edad = 21
estudiante = True

print (f"Hola, Me llamo {nombre}, tengo { edad } y es { estudiante} que soy estudiante")
edad_str = str(edad)
print(f"Mi edad es {edad} años")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

nota = 85
if nota >= 90:
    print("Sobresaliente")
elif nota >=70:
    print("Notable")
else:
    print("Mejorable")