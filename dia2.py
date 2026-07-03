print("While")
contador = 0
while contador < 5:
    print(f" contador = {contador}")
    contador += 1

print("-------------For---------------")
frutas = ("manzana", "banana", "cherry", "uva")
for fruta in frutas:
    print(f" fruta: {fruta}")

print("-------------For con Range-----")
for i in range(5):
    print(f" i = {i}")

print("Ejercicio #2")
for i in range (2,8):
    print(f"i = {i}")

print("Ejercicio #3")
for i in range (0, 10, 2):
    print(f" pares: {i}")

print("For con Diccionario")
persona = {
    "nombre" : "Johnier",
    "edad" : 21,
    "ciudad" : "El corazon de mi amor"
}
for clave, valor in persona.items():
    print(f" {clave}:{valor}")

print("Ejercicio #2")
for i in range(3):
    for j in range(2):
        print(f" i={i}, j={j}  ")
