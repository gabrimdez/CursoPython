#Ejercicio 1, Crea una lista con los números del 1 al 5 e imprímela.

list1 = [1, 2, 3, 4, 5]
print(list1)

#Ejercicio 2, Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

list2 = [10, 20, 30, 40, 50]
print(list2[2])

#Ejercicio 3, Agrega el número 6 al final de la lista del Ejercicio 1 e imprímela.

list1.append(6)
print(list1)

#Ejercicio 4, Inserta el número 15 en la posición 2 de la lista del Ejercicio 2 e imprímela.

list2.insert(2, 15)
print(list2)

#Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
list3 = [10, 20, 30, 30, 40, 50]
list3.remove(30)

"""
Usa la función pop() para eliminar el último elemento de
la lista [1, 2, 3, 4, 5] y almacénalo en una variable.
Imprime la variable y la lista.
"""
list4 = [1, 2, 3, 4, 5]
ultimo_elemento = list4.pop()
print(list4)

#Invierte la lista [100, 200, 300, 400, 500] e imprímela.
list5 = [100, 200, 300, 400, 500]
list5.reverse()
print(list5)

#Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
list6 = [3, 1, 4, 2, 5]
list6.sort()
print(list6)

"""
Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el
resultado en una nueva lista. Imprime la lista
resultante.
"""
list7 = [1, 2, 3]
list8 = [4, 5, 6]
list9 = list7 + list8
print(list9)

"""Crea una sublista con los elementos de la lista
[10, 20, 30, 40, 50] que van desde la posición 1 hasta
la 3 (sin incluir la posición 3)."""
list10 = [10, 20, 30, 40, 50]
sublista = list10[1:3]
print(sublista)