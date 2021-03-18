# Programa De lenguaje Natural

import re

knowledge = []

def readFile():
    f = open("info.txt", "r")
    for line in f:
        if line[0] == '#':
            pass
        else:
            palabras = line.split(",")
            knowledge.append(palabras)

def process(consulta):
    consultaSanitzed = re.sub("[,¿?]","", consulta)
    consultaSanitzed = consultaSanitzed.split()
    search(consultaSanitzed)

def search(palabras):
    resul = []
    for element in knowledge:
        if element[0] in palabras and element[1] in palabras:
            resul.append(element)
            print(element[2])
        else:
            pass
    if resul == []:
        print("No entiendo tu pregunta")

if __name__ == '__main__':
    readFile()
    print("Ingrese su consulta")
    consulta = input()
    process(consulta)
