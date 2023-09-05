size = 8
posicion = True
tablero = [[0 for _ in range(size)] for _ in range(size)]

while posicion:

    print("Ingrese las coordenadas a las que se encuentra el caballo")
    ejex = int(input("Fila (de 1 a 8): "))
    ejey = int(input("Columna (de 1 a 8): "))
    if ejex > 8 or ejex < 1 or ejey > 8 or ejey < 1:
        posicion = True
        print("La posición es inválida (fuera del tablero 8 x 8)")
    else:
        posicion = False

size = 8
posicion = True
tablero = [[0 for _ in range(size)] for _ in range(size)]

ejex -= 1
ejey -= 1
tablero[ejex][ejey] = 2

if (
        ejex + 2 <= 7
        and ejex - 2 >= 0
        and ejey + 2 <= 7
        and ejey - 2 >= 0
):
    tablero[ejex + 1][ejey + 2] = 1
    tablero[ejex + 2][ejey + 1] = 1
    tablero[ejex + 2][ejey - 1] = 1
    tablero[ejex + 1][ejey - 2] = 1
    tablero[ejex - 1][ejey - 2] = 1
    tablero[ejex - 2][ejey - 1] = 1
    tablero[ejex - 2][ejey + 1] = 1
    tablero[ejex - 1][ejey + 2] = 1
elif ejex + 2 > 7:
    if ejey + 2 > 7:
        tablero[ejex - 1][ejey - 2] = 1
        tablero[ejex - 2][ejey - 1] = 1
    elif ejey - 2 < 0:
        tablero[ejex - 2][ejey + 1] = 1
        tablero[ejex - 1][ejey + 2] = 1
    else:
        tablero[ejex - 1][ejey - 2] = 1
        tablero[ejex - 2][ejey - 1] = 1
        tablero[ejex - 2][ejey + 1] = 1
        tablero[ejex - 1][ejey + 2] = 1
elif ejex - 2 < 0:
    if ejey - 2 < 0:
        tablero[ejex + 1][ejey + 2] = 1
        tablero[ejex + 2][ejey + 1] = 1
    elif ejey + 2 > 7:
        tablero[ejex + 2][ejey - 1] = 1
        tablero[ejex + 1][ejey - 2] = 1
    else:
        tablero[ejex + 1][ejey + 2] = 1
        tablero[ejex + 2][ejey + 1] = 1
        tablero[ejex + 2][ejey - 1] = 1
        tablero[ejex + 1][ejey - 2] = 1

for fila in tablero:
    print(" ".join(map(str, fila)))

for i in range(size):
    for j in range(size):
        if tablero[i][j] == 1:
            print(f"Fila: {i+1} columna: {j+1}")

print("El número 2 en el tablero representa la posición actual del caballo")
print("UwU")
