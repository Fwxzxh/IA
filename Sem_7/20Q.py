# 20Q
# 1. buscar archivo csv para tomar de alli la información
# 2. con ese archivo formular las preguntas
# 3. generar las estructuras de datos

import csv

data = []
candidatos = []


def readCsv(option):
    datasets = ("Data/small.csv","Data/medium.csv","Data/big.csv")
    if option in [1,2,3]:
        with open(datasets[option-1], newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    else:
        raise Exception("Opción de tamaño invalida")


def ask():
    numPreguntas = len(data[0])
    for i in range(0,numPreguntas):
        print(data[0][i])


if __name__ == '__main__':
    print("Bienvenido a 20Q!")
    print("Seleccione el tamaño del dataSet: 1-Small, 2-Medium, 3-Big")
    option = int(input())
    readCsv(option)
    ask()
    pass
