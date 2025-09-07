ed = int(input("dame tu edad: "))
if ed < 0:
    print("edad no válida. Por favor ingresa un número positivo.")
else:
    if ed < 12:
        tarifa = 50
    elif ed <= 17:
        tarifa = 80
    else:
        tarifa = 120
    print(f"el costo de entrada es: ${tarifa}")

