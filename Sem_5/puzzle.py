# implementación de la resolución del puzzle de 8
# empezamos desde el 1?
#

from os import system, name

def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')


def printPuzzle(puzzle):
    for i in range(3):
        for j in range(3):
            print(puzzle[i][j], end='')
        print(' ')


def soluciona():
    pass


if (__name__=="__main__"):
    print("¿Desea ingresar el puzzle manualmente o usar el predeterminado? Si:1 No:0")
    n = int(input())
    if (n==1):
        puzzle = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                clear()
                printPuzzle(puzzle)
                print(f"Ingrese el valor de ({i},{j})")
                puzzle[i][j] = int(input())
    else:
        # puzzle demo
        puzzle = [[2,8,1],
                  [0,4,3],
                  [7,6,5]]
        pass
