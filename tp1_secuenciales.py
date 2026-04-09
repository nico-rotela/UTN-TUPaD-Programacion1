# ejercicio 1
print("hola mundo")

# ejercicio 2
nombre = input("ingrese su nombre:")
print(f"hola {nombre}")

# ejercicio 3
nombre = input ("hola ingrese su nombre:")
apellido = input("ingrese su apellido:")
edad = input("cuantos años tiene?:")
residencia = input("donde vive?:")

print(f"te llamas {nombre} {apellido}, tenes {edad} años y vivis en {residencia}")

# ejercicio 4
pi = 3.1416

radio = float(input("ingrese el radio del circulo: "))

perimetro = 2 * pi * radio

area = pi * radio ** 2

print(f"el perimetro del circulo es: {perimetro}")
print(f"el area del circulo es: {area}")

# ejercicio 5
segundos = int(input("ingrese la cantidad de segundos: "))

horas = segundos / 3600

print(f"la cantidad de horas es: {horas}")

# ejercicio 6
numero = int(input("ingreese un numero: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# ejercicio 7
numero1 = int(input("Ingrese el primer número (distinto de 0): "))
numero2 = int(input("Ingrese el segundo número (distinto de 0): "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"Resultado Suma: {suma}")
print(f"Resultado División: {division}")
print(f"Resultado Multiplicación: {multiplicacion}")
print(f"Resultado Resta: {resta}")

# ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal es: {imc}")

# ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# ejercicio 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los números ingresados es: {promedio}")