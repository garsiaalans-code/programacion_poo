lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("ahora del segundo: "))
lado3 = float(input("tambien del tercero: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("triángulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("triángulo isósceles.")
    else:
        print("triángulo escaleno.")
else:
        print("error")
