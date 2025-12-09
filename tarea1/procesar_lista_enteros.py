def procesar_lista_enteros(lista_original):
    # 1. Eliminar los números negativos de la lista.
    # Filtramos solo los números que son mayores o iguales a cero.
    numeros_positivos = [num for num in lista_original if num >= 0]

    # 2. Eliminar los valores que están repetidos, quedándonos con uno de ellos.
    # Convertimos la lista a un conjunto para eliminar duplicados automáticamente.
    # Luego, la convertimos de nuevo a una lista.
    lista_sin_duplicados = list(set(numeros_positivos))

    # 3. Ordenar los números resultantes de menor a mayor.
    # Usamos la función sorted() para ordenar la lista.
    lista_final_ordenada = sorted(lista_sin_duplicados)
 

    return lista_final_ordenada
