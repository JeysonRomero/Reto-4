# Pedir al usuario que ingrese un número real
x = float(input("Ingrese un número real: "))

# Determinar si el número es positivo, negativo o cero
if x > 0:
    print(f"El número {x} es positivo.")
elif x < 0:
    print(f"El número {x} es negativo.")
else:
    print(f"El número {x} es el neutro para la suma.")
