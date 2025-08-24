# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.

numero = float(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.

edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.

cadena = input("Introduce una cadena de texto: ")
if cadena:
    print("La cadena no está vacía.")
else:
    print("La cadena está vacía.")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
elif num1 < num2:
    print("El segundo número es mayor.")
else:
    print("Los números son iguales.")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.

numero = int(input("Introduce un número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("El número es divisible por 3 y por 5.")
else:
    print("El número no es divisible por 3 y por 5.")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.

numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). 
# Si tiene 16 o 17 años, indica que puede votar con permiso especial.

edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Puedes votar.")
elif edad == 16 or edad == 17:
    print("Puedes votar con permiso especial.")
else:
    print("No puedes votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. 
# Si no coincide, muestra un mensaje de error.

contrasena_predefinida = "1223"
contrasena_usuario = input("Introduce la contraseña: ")

if contrasena_usuario == contrasena_predefinida:
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).

numero = int(input("Introduce un número: "))
if 10 <= numero <= 20:
    print("El número está entre 10 y 20.")
else:
    print("El número no está entre 10 y 20.")   

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un 
# color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

color = input("Introduce el color del semáforo (rojo, amarillo, verde): ")

if color == "rojo":
    print("Debes detenerte.")
elif color == "amarillo":
    print("Debes estar alerta.")
elif color == "verde":
    print("Puedes avanzar.")
else:
    print("Color no válido.")
