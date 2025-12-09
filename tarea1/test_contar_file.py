# --- Pequeño programa para poner a prueba la función ---

# 1. Crear un archivo de texto de ejemplo
nombre_fichero_prueba = "mi_fichero_ejemplo.txt"
contenido_ejemplo = """
Hola mundo, este es un ejemplo de texto para probar la función. 
El mundo es grande y hola es una palabra común. 
Ejemplo, ejemplo, MUNDO.
"""

with open(nombre_fichero_prueba, 'w', encoding='utf-8') as f:
    f.write(contenido_ejemplo)

print(f"Archivo '{nombre_fichero_prueba}' creado con éxito.")

# 2. Definir la lista de palabras a buscar
palabras_a_buscar = input("palabras a buscar separadas por comas").split()

# 3. Llamar a la función
resultado_frecuencias = contar_palabras_fichero(
    palabras_a_buscar, nombre_fichero_prueba
)

# 4. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.
print("\nFrecuencia de palabras en el archivo (ordenado alfabéticamente):")
if resultado_frecuencias:
    for palabra, frecuencia in sorted(resultado_frecuencias.items()):
        print(f"'{palabra}': {frecuencia} veces")
else:
    print("No se encontraron las palabras buscadas o el archivo está vacío/no existe.")
