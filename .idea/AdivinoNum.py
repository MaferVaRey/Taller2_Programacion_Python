import random

NumAleatorio = random.randint(1, 100)
contador = 0
intento = 0
Intentos = []

print("El programa pensó un número del 1 al 100. Intente adivinarlo en la menor cantidad de intentos posibles")

while intento != NumAleatorio:
    contador += 1
    print("Intento " + str(contador) + ":")
    intento = int(input())
    Intentos.append(intento)

    if intento > NumAleatorio:
        print("El número es menor que " + str(intento))
    elif intento < NumAleatorio:
        print("El número es mayor que " + str(intento))

print("Felicitaciones, el número era: " + str(NumAleatorio))
print("Usted adivinó en " + str(contador) + " intentos")

for i in range(len(Intentos)):
    print("intento " + str(i+1) + ": " + str(Intentos[i]))