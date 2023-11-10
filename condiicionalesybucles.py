import random

# Ejercicio 1

numero = int(input("Ingrese un número: "))
suma_pares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de los números pares desde 1 hasta {numero} es: {suma_pares}")


# Ejercicio 2

palabra = input("Ingrese una palabra: ")
contador_vocales = 0
indice = 0

while indice < len(palabra):
    letra = palabra[indice].lower() 
    if letra in "aeiou":
        contador_vocales += 1
    indice += 1
print(f"La cantidad de vocales en la cadena es: {contador_vocales}")



# Ejercicio 3

numero = int(input("Ingrese un número: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"{numero} Es un número primo...")
else:
    print(f"{numero} No es un número primo!!!")


# Ejercicio 4

numero_secreto = random.randint(1, 100)

print("¡¡¡Bienvenido al juego!!!")
intentos = 0

while True:
    intento = int(input("Ingrese un número: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡¡¡Excelente!!! ¡Haz adivinado el número en {intentos} intentos!")
        break
    elif intento < numero_secreto:
        print("Demasiado Bajo...")
    else:
        print("Demasiado Alto...")


# Ejercicio 5

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    for _ in range(numero):
        print("*")
else:
    for i in range(1, numero + 1):
        print("* " * i)

