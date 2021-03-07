# Objetivos
# 1. Lista de todas las palabras usadas en un archivo
# 2. Palabras que le pueden segir a una palabra dada
# =============

from collections import defaultdict
import re
from random import randint

palabras_totales = 0
palabras = [{"Palabra": "", "Frecuencia": 0}]
knowledge = defaultdict(lambda: list())
#seed(time.gmtime) #pseudorandoms goes brrrrrr


def leerArchivo():
    poema = open("texto1.txt")
    linea = poema.readline()
    while linea != '':
        linea = poema.readline()
        aprendeTexto(linea)
        for palabra in list(linea.split()):
            x = re.sub("\W", "", palabra) #regex
            procesa(x.upper())


def procesa(palabra):
    global palabras_totales
    palabras_totales += 1
    item = next((item for item in palabras if item["Palabra"] == palabra), {"Palabra": "nones"}) #BRUHHHHHHHH! palabra is sus O.O/
    index = next((i for i, item in enumerate(palabras) if item["Palabra"] == palabra), -1)
    if item["Palabra"] == "nones":
        palabras.append({"Palabra": palabra, "Frecuencia": 1})
    else:
        n = palabras[index]["Frecuencia"]
        palabras[index]["Frecuencia"] = n+1


def printFrecuencias():
    for palabra in palabras: #grep & wc 4 the win
        print(palabra)
    n = len(palabras)
    print(f"Palabras unicas: {n}")


def aprendePalabra(previa, siguiente):
    global knowledge
    knowledge[previa].append(siguiente) #hate this <---


def aprendeTexto(linea):
    frase = linea.split()
    for i, palabra in enumerate(frase):
        if i == 0:
            aprendePalabra(("START","START"),palabra)
            continue
        if i == 1:
            aprendePalabra(("START",frase[0]),palabra)
            continue
        aprendePalabra((frase[i-2],frase[i-1]),palabra)
    pass


def escribeTexto():
    palabra = list()
    estado = 'START', 'START'
    while True:
        candidatos = knowledge[estado] # BAD!BAD!BAD code warning
        n = len(candidatos)
        if n == 0:
            break
        indice = randint(0, n) if n>1 else 0
        indice = indice -1 if n == indice else indice
        w = candidatos[indice]
        palabra.append(w)
        estado = estado[1], w
    return palabra


def creaPoema():
    print("\n") #C00L
    print("    _|_  _ |  _._ o _ ._")
    print("   (_| |(/_|<_>|_)|(/_|")
    print("               |")
    print("\n")
    print("Ingrese el numero de versos que desea:")
    versos = int(input())
    print("======================================")
    salida = ""
    n = 0
    while n <= versos:
        verso = escribeTexto()
        for palabra in verso:
            salida += palabra+" "
        print(salida+"\n")
        salida = ""
        n += 1


if (__name__ == "__main__"):
    leerArchivo()
    creaPoema()
    print("======================================")
    print("Desea la lista de palabras? si:1 no:0")
    lista = int(input())
    if lista == 1:
        printFrecuencias()
    else:
        pass
    #print(knowledge)
