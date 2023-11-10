# Ejercicio 1

numero = int(input("digita un número: "))

if numero % 2 == 0:
    print(numero, "es un número Par...")
else:
    print(numero, " es un numero Impar...")



# Ejercicio 2

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor...")




# Ejercicio 3

eda = int(input("Ingresa tu edad: "))
precio = int(input("Ingresa el precio del producto: "))

if eda < 18:
    resultado = precio * 0.90
    print("Su total a pagar es de: " ,resultado)
elif eda >= 65:
    resultado = precio * 0.85
    print("Su total a pagar es de: " ,resultado)
else:
    print("Su total a pagar es de: " ,precio)




# Ejercicio 4

puntuacion = int(input("Ingresa una puntuación (0/100): "))

if puntuacion >= 90 and puntuacion <= 100:
    print("Su puntuación " , puntuacion , "es A...Sobresaliente...")
elif puntuacion >= 80 and puntuacion <=89:
    print("Su puntuación " , puntuacion , "es B...Bueno...")
elif puntuacion >= 70 and puntuacion <=79:
    print("Su puntuación " , puntuacion , "es C...Satisfactorio...")
elif puntuacion >= 60 and puntuacion <=69:
    print("Su puntuación " , puntuacion , "es D...Necesita Mejorar...")
elif puntuacion < 60:
    print("Su puntuación " , puntuacion , "es F...Reprobado...")
elif puntuacion > 100:
    print("El puntaje ingresado es incorrecto!!!")



# Ejercicio 5

salario = int(input("Ingresa tu salario: "))

if salario <= 10000:
    print("No se te aplica descuento...")
elif salario > 10000 and salario <= 50000:
    renta = salario * 0.10
    print("tu impuesto a pagar es de: ", renta)
elif salario > 50000 and salario <= 100000:
    renta = salario * 0.20
    print("tu impuesto a pagar es de: ", renta)
elif salario > 100000:
    renta = salario * 0.30
    print("tu impuesto a pagar es de: ", renta)
