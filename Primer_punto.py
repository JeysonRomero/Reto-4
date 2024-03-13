
numero = int(input("Ingrese un número entero: "))

# Códigos ASCII de las vocales minúsculas
vocales = [97, 101, 105, 111, 117]

if numero in vocales:
    print(f"El número {numero} corresponde al código ASCII de una vocal minúscula.")
else:
    print(f"El número {numero} no corresponde al código ASCII de una vocal minúscula.")
