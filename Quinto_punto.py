import math

# Definir el centro y el radio del círculo
centro_x = float(input("Ingrese la coordenada x del centro del círculo: "))
centro_y = float(input("Ingrese la coordenada y del centro del círculo: "))
radio = float(input("Ingrese el radio del círculo: "))

# Definir las coordenadas del punto
punto_x = float(input("Ingrese la coordenada x del punto: "))
punto_y = float(input("Ingrese la coordenada y del punto: "))

# Calcular la distancia entre el centro del círculo y el punto
distancia_centro_punto = math.sqrt((punto_x - centro_x) ** 2 + (punto_y - centro_y) ** 2)

# Verificar si el punto está dentro del círculo
if distancia_centro_punto <= radio:
    print("El punto está dentro del círculo.")
else:
    print("El punto no está dentro del círculo.")
