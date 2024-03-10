# Reto-4

<br>

### 1. Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.

```
numero = int(input("Ingrese un número entero: "))

# Códigos ASCII de las vocales minúsculas
vocales = [97, 101, 105, 111, 117]

if numero in vocales:
    print(f"El número {numero} corresponde al código ASCII de una vocal minúscula.")
else:
    print(f"El número {numero} no corresponde al código ASCII de una vocal minúscula.")
```

se cumplio con el funcionamiento de este codigo con buenos resultados


![Captura de pantalla 2024-03-09 200536](https://github.com/JeysonRomero/Reto-4/assets/159095091/88b0c0e3-03b3-4136-b426-b99115486c31)


![Captura de pantalla 2024-03-09 200510](https://github.com/JeysonRomero/Reto-4/assets/159095091/b2404307-a3e9-4d1b-9b14-4ac36ad00dce)

<br>

### 2. Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.

```
# Solicitar al usuario que ingrese una cadena de longitud 1
cadena = input("Ingrese una cadena de longitud 1: ")

# Obtener el código ASCII de la primera letra de la cadena
codigo_ascii = ord(cadena[0])

# Verificar si el código ASCII es par o impar
if codigo_ascii % 2 == 0:
    print(f"El código ASCII de '{cadena[0]}' es par: {codigo_ascii}")
else:
    print(f"El código ASCII de '{cadena[0]}' es impar: {codigo_ascii}")
```

se cumplio con el funcionamiento de este codigo con buenos resultados


![Captura de pantalla 2024-03-09 201626](https://github.com/JeysonRomero/Reto-4/assets/159095091/1525329d-5d5f-4c6b-bbe0-a15e779724a4)

![Captura de pantalla 2024-03-09 201655](https://github.com/JeysonRomero/Reto-4/assets/159095091/dc9a5d38-dfdb-4441-baea-69f19b27e22e)

<br>

### 3. Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.

```
caracter = input("Ingresa un caracter: ")

if caracter.isdigit():
    print(f"'{caracter}' es un dígito.")
else:
    print(f"'{caracter}' no es un dígito.")

```

se cumplio con el funcionamiento de este codigo con buenos resultados

![Captura de pantalla 2024-03-09 202702](https://github.com/JeysonRomero/Reto-4/assets/159095091/f963eff6-f366-4c94-9557-aa68792d9d24)
![Captura de pantalla 2024-03-09 202517](https://github.com/JeysonRomero/Reto-4/assets/159095091/3663143c-f78f-46a8-9a76-2a80fc02dad3)

<br>

### 4.Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:



```
# Pedir al usuario que ingrese un número real
x = float(input("Ingrese un número real: "))

# Determinar si el número es positivo, negativo o cero
if x > 0:
    print(f"El número {x} es positivo.")
elif x < 0:
    print(f"El número {x} es negativo.")
else:
    print(f"El número {x} es el neutro para la suma.")
```

<br>

se cumplio con el funcionamiento de este codigo con buenos resultados

<br>

![Captura de pantalla 2024-03-09 203223](https://github.com/JeysonRomero/Reto-4/assets/159095091/1a0ae983-434f-47b1-9aa8-6d50e8a54372)
![Captura de pantalla 2024-03-09 203159](https://github.com/JeysonRomero/Reto-4/assets/159095091/7838b3ad-9527-4501-976d-19d51403bc20)
![Captura de pantalla 2024-03-09 203159](https://github.com/JeysonRomero/Reto-4/assets/159095091/1c8089ff-8e98-422e-a6f0-f818ad2cdf54)


### 5.Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.


```
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
```

<br>

se cumplio con el funcionamiento de este codigo con buenos resultados

<br>

![Captura de pantalla 2024-03-09 204010](https://github.com/JeysonRomero/Reto-4/assets/159095091/8e4aa8cf-927b-4dcf-bfbb-d3ddb93e58b3)


### 6.Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.

```
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

```
<br>

![Captura de pantalla 2024-03-09 204549](https://github.com/JeysonRomero/Reto-4/assets/159095091/79808533-3fca-4c7f-9337-59ed99614abd)





