print("¿Cuántos datos serán ingresados?")
tamano = int(input())
numeros = []

for i in range(tamano):
    print("Ingrese el " + str(i+1) + " número")
    numeros.append(int(input()))

numeros.sort()
rango = int(numeros[-1] - numeros[0])

print("El rango es:", rango)
