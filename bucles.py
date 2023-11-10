import random

# Ejercicio 1

asc = 0
des = 11

while asc < 10:
    asc += 1
    des -= 1
    print(asc, des)


# Ejercicio 2

aleatorio = random.randint(1, 100)
adivina = 0

while adivina != aleatorio:
    if adivina == 0:
        print("Inicia el juego")
    elif adivina < aleatorio:
        print("Demasiado bajo")
    else:
        print("Demasiado Alto")
    adivina = int(input("Ingresa el número: "))



# Ejercicio 3

numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")

i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1



# Ejercicio 4

num = int(input("Ingrese un número: "))
suma_pares = 0

for i in range(1, num + 1,):
    if i % 2 == 0:
        suma_pares += i
    print(f"La suma de todos los números pares desde 2 hasta {num} es: {suma_pares}")



# Ejercicio 5

n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")