def contar_palabras():
    # Convertir el texto a minúsculas para hacer la comparación de palabras más fácil
    texto = input("Por favor, ingresa una frase o párrafo: ")

    # Reemplazar signos de puntuación comunes con espacios
    for signo in [",", ".", ":", ";", "!", "¿","?", "(", ")"]:
        texto = texto.replace(signo, " ")
    
    # Separar el texto en palabras
    palabras = texto.split()
    
    # Crear un diccionario para contar las palabras
    conteo_palabras = {}
    
    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1
    
    # Obtener una lista de palabras ordenadas alfabéticamente
    palabras_ordenadas = sorted(conteo_palabras.keys())
    
    # Imprimir cada palabra y su conteo
    for palabra in palabras_ordenadas:
        print(f"{palabra}: {conteo_palabras[palabra]}")
        
