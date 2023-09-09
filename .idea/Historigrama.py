numeros_positivos = []
numeros_negativos = []

print("A continuación, ingrese tantos números enteros como desee. Al finalizar, ingrese 0")

while True:
    numero = int(input("Ingrese el número: "))
    if numero == 0:
        break
    elif numero > 0:
        numeros_positivos.append(numero)
    elif numero < 0:
        numeros_negativos.append(numero)

print("Números positivos:", "*" * len(numeros_positivos))
print("Números negativos:", "*" * len(numeros_negativos))
