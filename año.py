añito = int(input("dame el año"))
if (añito % 4 == 0 and añito % 100 != 0) or (añito% 400 == 0):
    print(f"{añito} es año bisiesto.")
else:
    print(f"{añito} no es año bisiesto.")
