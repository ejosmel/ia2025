def procesar_conjuntos():
    # Solicitar el primer conjunto de números
    conjunto1 = input("Introduce el primer conjunto de números separados por comas: ")
    # Convertir la entrada en un conjunto de enteros
    conjunto1 = set(map(int, conjunto1.split(',')))
    
    # Solicitar el segundo conjunto de números
    conjunto2 = input("Introduce el segundo conjunto de números separados por comas: ")
    # Convertir la entrada en un conjunto de enteros
    conjunto2 = set(map(int, conjunto2.split(',')))
    
    # Calcular la intersección (elementos comunes)
    interseccion = conjunto1 & conjunto2
    
    # Calcular la unión (todos los elementos sin duplicados)
    union = conjunto1 | conjunto2
    
    # Calcular la diferencia simétrica (elementos que están en uno u otro, pero no en ambos)
    diferencia_simetrica = conjunto1 ^ conjunto2
    
    # Mostrar los resultados
    print(f"Intersección: {sorted(interseccion)}")
    print(f"Unión: {sorted(union)}")
    print(f"Diferencia simétrica: {sorted(diferencia_simetrica)}")
