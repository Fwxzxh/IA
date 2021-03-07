# Sudoku solving w Backtraking

from os import system, name


def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_grid(arr, input=False, x=0, y=0):
    for i in range(9):
        for j in range(9):
            num = str(arr[i][j]) if arr[i][j] != -1 else "+"
            if (input):
                if (i==x and j==y):
                    if (j==2 or j==5):
                        print("_", end=' | ')
                    else:
                        print("_", end=' ')
                else:
                    if (j==2 or j==5):
                        print(num, end=' | ')
                    else:
                        print(num, end=' ')
            else:
                if (j==2 or j==5):
                    print(num, end=' | ')
                else:
                    print(num, end=' ')
        print(' ')
        if (i==2 or i == 5):
            print("------+-------+------")


def busca_lugar_vacio(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col]==0):
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if (arr[col][i] == num):
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, row, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)


def resuelve_sudoku(arr):
    l = [0, 0]
    if (not busca_lugar_vacio(arr, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if (check_location_is_safe(arr, row, col, num)):
            arr[row][col] = num
            if (resuelve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False


if (__name__ == "__main__"):
    print("¿Desea introducir un sudoku manualmente o usar el de muestra? Si:1 No:0")
    answer = int(input())
    if (answer == 1):
        grid = [[-1 for _ in range(9)] for _ in range(9)]
        print("Ingrese los valores del sudoku, en las casillas vacias ingrese el numero '0'")
        for i in range(9):
            for j in range(9):
                print_grid(grid, True, i, j)
                print(f"Ingrese el valor en la columna ({i}, {j})")
                grid[i][j] = int(input())
                clear()
    else:
        # default grid
        grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
               [5, 2, 0, 0, 0, 0, 0, 0, 0],
               [0, 8, 7, 0, 0, 0, 0, 3, 1],
               [0, 0, 3, 0, 1, 0, 0, 8, 0],
               [9, 0, 0, 8, 6, 3, 0, 0, 5],
               [0, 5, 0, 0, 9, 0, 6, 0, 0],
               [1, 3, 0, 0, 0, 0, 2, 5, 0],
               [0, 0, 0, 0, 0, 0, 0, 7, 4],
               [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if (resuelve_sudoku(grid)):
        print_grid(grid)
    else:
        print ("¡¡No existen soluciones!! (╯°□°）╯︵ ┻━┻")
