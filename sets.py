## 1. Crea un set con los números del 1 al 5 e imprímelo.
mi_set = {1, 2, 3, 4, 5}
print(mi_set)

## 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
mi_set.add(6)
print(mi_set)

## 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
mi_set.add(5)
print(mi_set)

## 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in mi_set)

## 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
mi_set.remove(4)
print(mi_set)

## 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
mi_set.clear()
print(len(mi_set))

## 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
mi_set = {"manzana", "naranja", "plátano"}
mi_lista = list(mi_set)
print(mi_lista[0])

## 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set_union = set1.union(set2)
print(set_union)

## 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
set_difference = set3.difference(set4)
print(set_difference)

## 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = {1, 2, 3}
del my_set
#print(my_set)
