# Redes neuronales
# Crear una red neuronal generica donde puedas especificar el numero de entradas y el numero de neuronas en cada capa (opcional, permitir una o más capas ocultas)
# 1. Una capa recibe valores
# 2. Se realiza una suma ponderada de todos los valores de entrada
# 3. Al resultado se le sumara otro parametro conocido como Bias (b) cada neurona tiene el suyo
# 4. Función de activación

import numpy as np

# Funciones de activación
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoidDerivada(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanhDerivada(x):
    return 1.0 - x**2

def getDatos():
    topologia = []
    topologia.append(int(input("Ingrese el número de entradas de la red neuronal: ")))
    n = int(input("Ingrese el número de neuronas por capa: "))
    p = int(input("Ingrese el número de capas ocultas: "))
    for _ in range(p):
        topologia.append(n)
    topologia.append(int(input("Ingrese el número de salidas: ")))
    return topologia

def test():
    # funcion Coche Evita obstáculos
    nn = RedNeuronal([2,3,2], fActivacion= 'tanh')
    X = np.array([[0, 0],   # sin obstaculos
                [0, 1],   # sin obstaculos
                [0, -1],  # sin obstaculos
                [0.5, 1], # obstaculo detectado a derecha
                [0.5,-1], # obstaculo a izq
                [1,1],    # demasiado cerca a derecha
                [1,-1]])  # demasiado cerca a izq

    y = np.array([[0,1],    # avanzar
                [0,1],    # avanzar
                [0,1],    # avanzar
                [-1,1],   # giro izquierda
                [1,1],    # giro derecha
                [0,-1],   # retroceder
                [0,-1]])  # retroceder
    nn.fit(X, y, learningRate=0.03,epochs=15001)

    index=0
    for e in X:
        print("X:",e,"y:",y[index],"Network:",nn.predict(e))
        index=index+1

    import matplotlib.pyplot as plt

    deltas = nn.getDeltas()
    valores=[]
    index=0
    for arreglo in deltas:
        valores.append(arreglo[1][0] + arreglo[1][1])
        index=index+1

    plt.plot(range(len(valores)), valores, color='b')
    plt.ylim([0, 1])
    plt.ylabel('Cost')
    plt.xlabel('Epochs')
    plt.tight_layout()
    plt.show()


def test1():
    nn = RedNeuronal([2,2,1])
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 1, 1, 0])
    nn.fit(X, y,epochs=2000)
    for e in X:
        print("Entrdas:",e,"Salidas:", nn.predict(e))

class RedNeuronal:
    def __init__(self, capas, fActivacion="tanh"):
        if fActivacion == "sigmoid":
            self.fActivacion = sigmoid
            self.fActivacionPrime = sigmoidDerivada
        if fActivacion == "tanh":
            self.fActivacion = tanh
            self.fActivacionPrime = tanhDerivada

        self.pesos = []
        self.deltas = []

        # inicializamos los pesos con valores random entre -1 y 1 en la capa de entrada y ocultas
        for i in range(1, len(capas) -1):
            r = 2**np.random.random((capas[i-1] + 1, capas[i] + 1)) - 1
            self.pesos.append(r)
        # pesos aleatorios en la capa de salida
        r = 2**np.random.random((capas[i] + 1, capas[i+1])) -1
        self.pesos.append(r)

    def fit(self, X, y, learningRate=0.2, epochs=10000):
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.pesos)):
                dotValue = np.dot(a[l], self.pesos[l])
                fActivacion = self.fActivacion(dotValue)
                a.append(fActivacion)

            # dif entre capa de salida y valor obtenido
            error = y[i] - a[-1]
            deltas = [error * self.fActivacionPrime(a[-1])]

            # desde una capa anterior a la salida
            for l in range(len(a) -2, 0, -1):
                deltas.append(deltas[-1].dot(self.pesos[l].T) * self.fActivacionPrime(a[l]))
            self.deltas.append(deltas)

            # invertir las deltas
            deltas.reverse()

            # backpropagation
            # 1. multiplicar los delta con las activaciones de entrada para obtener el gradiente del peso
            # 2. actualizamos el peso restandole un porcentaje del gradiente
            for i in range(len(self.pesos)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.pesos[i] += learningRate * layer.T.dot(delta)

            if k % 10000 == 0: print("epochs:", k)

    def predict(self, x):
        ones = np.atleast_2d(np.ones(x.shape[0]))
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)
        for l in range(0, len(self.pesos)):
            a = self.fActivacion(np.dot(a, self.pesos[l]))
        return a

    def printWeights(self):
        print("LISTADO PESOS DE CONEXIONES")
        for i in range(len(self.pesos)):
            print(self.pesos[i])

    def getDeltas(self):
        return self.deltas

if __name__ == '__main__':
    topologia = getDatos()
    nn = RedNeuronal(topologia)
    print(nn)
    #test()
    pass
