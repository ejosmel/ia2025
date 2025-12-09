def contar_palabras_fichero(lista_palabras, ruta_fichero):
    # 1. recuperamos el contenido del fichero en la variabla contenido pasandolo a minusculas
    try:
        with open(ruta_fichero, 'r', encoding='utf-8') as f:
            contenido = f.read().lower()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_fichero}' no fue encontrado.")
        return {}

    #  Reemplazar signos de puntuación comunes con espacios y dividir
    for signo in [",", ".", ":", ";", "!", "¿","?", "(", ")"]:
        contenido = contenido.replace(signo, " ")
    
    # creamos diccionario frecuencias a 0 para las palabras de interés
    lista_palabras_lower = [palabra.lower() for palabra in lista_palabras]
    frecuencias = {palabra:0 for palabra in lista_palabras_lower} 

    # 3. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
    lista_contenido =contenido.split()
    for palabra in lista_contenido:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

    return frecuencias
