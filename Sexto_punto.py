def es_triangulo(a, b, c):
    """
    Función para determinar si las longitudes a, b y c pueden formar un triángulo.
    """
    # Comprobar la desigualdad triangular
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Solicitar al usuario que ingrese las longitudes de los lados del triángulo
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Verificar si se puede construir un triángulo con las longitudes dadas
if es_triangulo(lado1, lado2, lado3):
    print("Se puede construir un triángulo con las longitudes dadas.")
else:
    print("No se puede construir un triángulo con las longitudes dadas.")

