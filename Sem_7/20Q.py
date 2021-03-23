# 20Q

import csv
from os import system, name

data = []
candidatos = []
preguntas = []
respuestas = []
option = 0
datasets = ("Data/small.csv","Data/medium.csv","Data/big.csv")

def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def readCsv(option):
    global datasets
    if option in [1,2,3]:
        with open(datasets[option-1], newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    else:
        raise Exception("Opción de tamaño invalida")


def processCsv():
    numPreguntas = len(data[0])
    numOpciones = len(data)
    for i in range(1, numPreguntas):
        preguntas.append(data[0][i])
    for i in range(1, numOpciones):
        candidatos.append(data[i][0])
    #print(candidatos, preguntas)
    ask(numPreguntas, numOpciones)


def ask(numP, numO):
    global candidatos, preguntas
    for i in range(1,numP):
        a = writeQuestion(preguntas.pop(0))
        respuestas.append(a)
        for j in range(1,numO):
            if (int(a) == int(data[j][i])):
                #print(candidatos[j-1], "aceptado")
                pass
            else:
                #print(candidatos[j-1], "descartado")
                candidatos[j-1] = None
    printResult(candidatos, numO)


def writeQuestion(pregunta):
    clear()
    print(pregunta)
    answer = input().upper()
    if answer == "YES":
        return 1
    else:
        return 0


def printResult(candidatos, numOpciones):
    findedAnswer = False
    for i in range(numOpciones):
        if candidatos[i-1] != None:
            findedAnswer = True
            print("El animal en el que piensas puede ser:",candidatos[i-1])
    if not findedAnswer:
        print("No encontre la respuesta :c")
        a = writeQuestion("Desea agregar su respuesta?")
        if a:
            print("Ingrese el nombre del animal de tus respuestas")
            a = input()
            addAnswer(a, respuestas)
        else:
            print("Gracias por jugar!")


def addAnswer(candidato, respuestas):
    #print(option, "answ")
    respuestas.insert(0, candidato)
    print("Escribiendo en el dataset", datasets[option-1])
    with open(datasets[option-1], mode='a', newline='') as csv_file:
        animal_writer = csv.writer(csv_file, dialect='unix')
        animal_writer.writerow(respuestas)
        pass


if __name__ == '__main__':
    print("Bienvenido a 20Q!")
    print("Responta Yes o No")
    print("Seleccione el tamaño del dataSet: 1-Small, 2-Medium, 3-Big")
    option = int(input())
    readCsv(option)
    processCsv()
