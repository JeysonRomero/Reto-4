# Solicitar al usuario que ingrese una cadena de longitud 1
cadena = input("Ingrese una cadena de longitud 1: ")

# Obtener el código ASCII de la primera letra de la cadena
codigo_ascii = ord(cadena[0])

# Verificar si el código ASCII es par o impar
if codigo_ascii % 2 == 0:
    print(f"El código ASCII de '{cadena[0]}' es par: {codigo_ascii}")
else:
    print(f"El código ASCII de '{cadena[0]}' es impar: {codigo_ascii}")
