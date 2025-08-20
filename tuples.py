# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
mi_tupla = (10, 20, 30, 40, 50)
print(mi_tupla)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muestralo

mi_tupla2 = (100, 200, 300, 400, 500)
print(mi_tupla2[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

# Si intentas modificar un elemento de una tupla en Python, obtendrás un error TypeError.
# Las tuplas son inmutables, lo que significa que no puedes cambiar, agregar ni eliminar sus elementos después de haberlas creado.

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
mi_tupla4 = (1, 2, 3, 3, 4, 5, 3)
print(mi_tupla4.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
mi_tupla5 = ("Java", "Python", "JavaScript", "Python")
print(mi_tupla5.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
mi_tupla6_1 = (1, 2, 3)
mi_tupla6_2 = (4, 5, 6)
mi_tupla6_resultado = mi_tupla6_1 + mi_tupla6_2
print(mi_tupla6_resultado)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
mi_tupla7 = (10, 20, 30, 40, 50)
mi_subtupla7 = mi_tupla7[2:4]
print(mi_subtupla7)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo"
# y vuelve a convertirla en una tupla. Imprime la tupla resultante.
mi_tupla8 = ("rojo", "verde", "azul")
mi_lista8 = list(mi_tupla8)
mi_lista8[1] = "amarillo"
mi_tupla8_resultado = tuple(mi_lista8)
print(mi_tupla8_resultado)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1, 2, 3)
del my_tuple
#print(my_tuple)  # Esto generará un error porque my_tuple ya no existe.

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela.
# Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
mi_tupla10 = (100)
print(mi_tupla10)
