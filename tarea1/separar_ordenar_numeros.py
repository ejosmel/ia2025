def separar_ordenar_numeros(lista_enteros):

    negativos = []
    positivos = []
    lista_enteros.sort()
    for numero in lista_enteros:
        if numero < 0:
            negativos.append(numero)
        elif numero > 0:
            positivos.append(numero)
    return negativos, positivos

# Ejemplo de uso:
# mi_lista = [3, -1, 0, 8, -5, 2, -10, 4]
# neg, pos = separar_y_ordenar_numeros(mi_lista)
# print("Negativos ordenados:", neg)  # Salida: [-10, -5, -1]
# print("Positivos ordenados:", pos)  # Salida: [2, 3, 4, 8]
