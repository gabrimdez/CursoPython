# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

persona = {
    "name": "Gabriel",
    "age": 19,
    "country": "España"
}

print(persona)

# 2. Accede al valor de la clave name en el diccionario.

print(persona["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

persona["job"] = "Programador"
print(persona)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
persona["age"] = 38
print(persona)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del persona["country"]
print(persona)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

cuadrados = {i: i**2 for i in range(1, 6)}
print(cuadrados)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Gabriel", "age": 19, "country": "España"}.

diccionario = {"name": "Gabriel", "age": 19, "country": "España"}
print("age" in diccionario)

# 8. Imprime solo las claves del diccionario.

print(diccionario.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
claves_lista = list(diccionario.keys())
print(claves_lista)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), 
# asignando a todas las claves el valor "Desconocido".

nuevas_claves = ["name", "age", "job"]
nuevo_diccionario = dict.fromkeys(nuevas_claves, "Desconocido")
print(nuevo_diccionario)

"""
Este script muestra ejemplos básicos de manipulación de diccionarios en Python:

1. Crea un diccionario con las claves 'name', 'age' y 'country', y muestra su contenido.
2. Accede y muestra el valor asociado a la clave 'name'.
3. Añade una nueva clave 'job' al diccionario y muestra el resultado.
4. Modifica el valor de la clave 'age' y muestra el diccionario actualizado.
5. Elimina la clave 'country' y muestra el diccionario resultante.
6. Crea un diccionario por comprensión donde las claves son números del 1 al 5 y los valores sus cuadrados.
7. Verifica si la clave 'age' está presente en un diccionario dado.
8. Imprime solo las claves del diccionario.
9. Convierte las claves del diccionario en una lista e imprime la lista.
10. Crea un nuevo diccionario a partir de una lista de claves usando 'fromkeys()', asignando a todas el valor "Desconocido".

Nota:
- La función 'dict.fromkeys(claves, valor)' crea un nuevo diccionario con las claves especificadas y asigna a todas ellas el mismo valor.
"""
