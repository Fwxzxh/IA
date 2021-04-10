# K-means from scratch

from dearpygui.core import *
from dearpygui.simple import *
import numpy as np
import random


def gen_Points(nPoints, nCluster):
    pointsX = []
    pointsY = []
    data = []
    for _ in range(nPoints):
        pointsX.append(random.randint(0,100))
        pointsY.append(random.randint(0,100))
    for i in range(nPoints):
        data.append([pointsX[i], pointsY[i]])
    add_scatter_series("Original Points", "",  pointsX, pointsY)
    kmeans(data, nPoints, nCluster, 50)


def plotZones(zonas):
    pointX = []
    pointY = []
    numZones = 0
    for zona in zonas:
        for elemento in zona:
            pointX.append(elemento[0])
            pointY.append(elemento[1])
        ranColor = list(np.random.randint(256, size=3)) + [255,]
        numZones += 1
        add_scatter_series("K-means draw", "zona "+ str(numZones), pointX, pointY, outline=ranColor)
        pointX = []
        pointY = []


def kmeans(data, nPoints, nCluster, nuIterations):
    # calcula los k-means
    indexCentroids = [] # array con los indices de los centroides
    centroids = []

    for _ in range(nCluster):
        indexCentroids.append(random.randint(0,nPoints-1)) # espero no se repitan (si paso, aaaaaaaaa)
    for i in indexCentroids:
        centroids.append(data[i])

    # start loop
    zonas = []
    for i in range(nuIterations):
        dist = getDist(centroids, nPoints, data)
        areas = compDist(nPoints, nCluster, dist)
        arrAreas = zip(data,areas)
        zonas = packZones(nCluster, nPoints, arrAreas)
        newCentroid = []
        for zona in zonas:
            newCentroid.append(getCentroid(zona))
        centroids = newCentroid
    plotZones(zonas)


def packZones(nCluster, nPoints, arrAreas):
    # retorna una lista con cada uno de los puntos agrupados en su respectivo cluster
    centroidZones = [[] for _ in range(nCluster)]

    a = list(arrAreas)
    for i in range(nCluster):
        for j in range(nPoints):
            if (a[j][1] == i):
                centroidZones[i].append(a[j][0])
    return centroidZones


def getCentroid(data):
    # Retorna el centroide optimizado de una lista de puntos (saca el promedio vaya!).
    x, y = zip(*data)
    l = len(x)
    return sum(x) / l, sum(y) / l


def getDist(centroids, nPoints, data):
    # retorna array de cada una de las distancias con respecto de los centroides
    dist = []
    for cent in centroids:
        for index in range(nPoints):
            dist.append([np.linalg.norm(cent[0] - data[index][0]), np.linalg.norm(cent[1] - data[index][1])])
    return dist


def compDist(nPoints, nCluster, dist):
    # retorna array con el indice de el centroide más cercano
    gap = 0
    comp = []
    cluster = []
    for i in range(nPoints):
        for _ in range(nCluster):
            comp.append(getAbsolutDist(dist[i + gap]))
            gap += nPoints
        cluster.append(comp.index(min(comp)))
        comp = []
        gap = 0
        i = i+1
    return(cluster)


def getAbsolutDist(dist):
    # retorna la distancia absoluta entre dos puntos
    return np.sqrt(dist[0] + dist[1])


with window("Points"):
    with tab_bar("PlotTabBar"):
        with tab("Original"):
            add_plot("Original Points")
        with tab("K-means"):
            add_plot("K-means draw")


if __name__ == '__main__':
    print("Ingrese el numero de puntos a generar")
    nPoints = int(input())
    print("Ingrese el numero de clusters a generar")
    nClusters = int(input())
    gen_Points(nPoints, nClusters)
    set_main_window_size(1000, 800)
    start_dearpygui()
    pass
