CA = int(input("dame tu calificación (0–100): "))
if 0 <= CA <= 100:
    if CA >= 90:
        letra = "A"
    elif CA >= 80:
        letra = "B"
    elif CA >= 70:
        letra = "C"
    elif CA >= 60:
        letra = "D"
    else:
        letra = "F"
    print(f"Tu calificación es: {letra}")
else:
    print("dame una cal valida")
