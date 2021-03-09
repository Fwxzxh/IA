# implementación del problema de rutas de R&N
# pag 87 del pdf
# pdf --> https://github.com/yanshengjia/ml-road/blob/master/resources/Artificial%20Intelligence%20-%20A%20Modern%20Approach%20(3rd%20Edition).pdf

#implementación del grafo de los caminos con listas de adyaciencia *Modo Serio*
numberVertix = 0
grapth = {}


def addVertex(v):
    global grapth
    global numberVertix
    if v in grapth:
        print("Vértice ", v, " Ya existe")
    else:
        numberVertix = numberVertix + 1
        grapth[v] = []


def addEdge(v1, v2, e):
    global grapth
    if v1 not in grapth:
        print("Vértice ", v1, " no existe")
    elif v2 not in grapth:
        print("Vértice ", v2, " no existe")
    else:
        # where everything comes together
        temp = [v2, e]
        grapth[v1].append(temp)


def printGrapth():
    global grapth
    global numberVertix
    for vertex in grapth:
        for edges in grapth[vertex]:
            print(vertex, " ==> ", edges[0], " distancia ", edges[1])
    print("Numero de vertices: ", numberVertix)
    print(grapth)


def createDefaultMap(): #just foll0w the lines, child!!
    addVertex("oradea")
    addVertex("zerind")
    addVertex("arad")
    addVertex("sibiu")
    addEdge("oradea", "sibiu", 151)
    addEdge("oradea", "zerind", 71)
    addEdge("zerind", "arad", 75)
    addEdge("arad", "sibiu", 140)
    addVertex("timisoara")
    addVertex("lugoj")
    addVertex("mehadia")
    addVertex("drobeta")
    addVertex("craiova")
    addEdge("arad", "timisoara", 118)
    addEdge("timisoara", "lugoj", 111)
    addEdge("lugoj", "mehadia", 70)
    addEdge("mehadia", "drobeta", 75)
    addEdge("drobeta", "craiova", 120)
    # rumania, what a lovely place!
    addVertex("rimnicu vilcea")
    addVertex("fragaras")
    addVertex("bucharest")
    addEdge("sibiu", "fragaras", 99)
    addEdge("fragaras", "bucharest", 211)
    addEdge("sibiu", "rimnicu vilcea", 80)
    addEdge("rimnicu vilcea", "craiova", 146)
    addVertex("pitesti")
    addEdge("craiova", "pitesti", 138)
    addEdge("pitesti", "bucharest", 101)
    addVertex("giurgiu") #lol
    addEdge("bucharest", "giurgiu", 90)
    addVertex("urziceni")
    addEdge("bucharest", "urziceni", 85)
    # last chunk
    addVertex("vaslui")
    addVertex("lasi") #fav
    addVertex("neamt")
    addEdge("urziceni", "vaslui", 142)
    addEdge("vaslui", "lasi", 92)
    addEdge("lasi", "neamt", 87)
    addVertex("hirsova")
    addVertex("eforie")
    addEdge("urziceni", "hirsova", 98)
    addEdge("hirsova", "eforie", 86)


if (__name__=="__main__"):
    createDefaultMap()
    print("-Programa de rutas de rumania-")
    print("¿Desea ver el mapa? Si:1 No:0")
    choice = int(input())
    if choice:
        printGrapth()
    else:
        print("duh~")
    # print("Ingrese el punto de salida, sin mayusculas")
    # inicio = input()
    # print("Ingrese el punto final")
    # final = input()
