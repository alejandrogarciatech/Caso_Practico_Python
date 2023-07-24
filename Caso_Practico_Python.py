"""Escribir un programa en Python que genere una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9. El programa deberá imprimir la matriz generada y luego calcular la suma de los elementos de cada fila y columna. Finalmente, deberá imprimir la suma de cada fila y columna.

El programa deberá incluir las siguientes características:

a) Generación de la matriz: El programa deberá generar una matriz cuadrada de tamaño NxN, donde N es un número entero ingresado por el usuario.
b) Rellenar la matriz con números aleatorios: El programa deberá rellenar la matriz con números aleatorios entre 0 y 9.
c) Imprimir la matriz: El programa deberá imprimir la matriz generada en pantalla.
d) Calcular la suma de cada fila y columna: El programa deberá calcular la suma de los elementos de cada fila y columna y almacenarlas en dos listas.
e) Imprimir la suma de cada fila y columna: El programa deberá imprimir en pantalla la suma de cada fila y columna.

Además, se sugiere que el programa incluya manejo de excepciones en caso de que el usuario ingrese un valor no válido para N, también que incluya comentarios para explicar el código y finalmente que se hagan los test unitarios necesarios para asegurar que el resultado es el esperado."""

import random #Importamos el módulo random para generar números aleatorios

try: #Comienza el bloque try para capturar posibles errores

    matriz = [] #Creamos una lista vacía para guardar los elementos de la matriz  
    n = int(input("Ingrese el tamaño de la matriz cuadrada: ")) #Pedimos al usuario el valor de N, el tamaño de la matriz
    if n <= 0:
        raise ValueError() #Si N es menor o igual a 0 se lanza una excepción ValueError

    matriz = [] #Vamos a llenar la lista matriz
    for i in range(n): #Recorremos la matriz desde la primera hasta la última posición (0, n-1) para generar filas
        fila = [] #Creamos una lista vacía para guardar los elementos de la fila
        for i in range(n): #Recorremos la fila de 0 a n-1 para generar elementos
            fila.append(random.randint(0, 9)) #Generamos números aleatorios entre 0 y 9 que se agregan a la fila
        matriz.append(fila) #Añadimos una fila a la matriz

    print("La matriz genereada es: ")
    for fila in matriz: #Para imprimir la matriz, primero recorremos todas sus filas
        print(fila) #e imprimimos cada una de ellas

    sumaFilas = []
    for fila in matriz:
        sumaFilas.append(sum(fila))

    sumaColumnas = []
    for i in range(n):
        columna = 0
        for fila in matriz:
            columna += fila[i]
        sumaColumnas.append(columna)

    print("Suma de cada fila: ", sumaFilas)
    print("Suma de cada columna: ", sumaColumnas)

except ValueError:
    print("Ingrese un número entero válido. Debe ser positivo y mayor que cero")
