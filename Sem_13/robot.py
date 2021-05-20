import RPi.GPIO as GPIO
import time

TRIG = 23 #Variable que contiene el GPIO al cual conectamos la señal TRIG del sensor
ECHO = 26 #Variable que contiene el GPIO al cual conectamos la señal ECHO del sensor

GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi
GPIO.setup(TRIG, GPIO.OUT) #Configuramos el pin TRIG como una salida
GPIO.setup(ECHO, GPIO.IN)  #Configuramos el pin ECHO como una salida

StepPins = [24,25,8,7] # Pins motor
for pin in StepPins:
    print("Setup pins")
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

# Define some settings
WaitTime = 0.005
# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = [i for i in range(0, StepCount1)]

Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

# Define advanced half-step sequence
StepCount2 = 8
Seq2 = []
Seq2 = [i for i in range(0, StepCount2)]

Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

# Choose a sequence to use
Seq = Seq2
StepCount = StepCount2

def steps(nb):
    StepCounter = 0
    if nb<0: sign=-1
    else: sign=1
    nb=sign*nb*2 #times 2 because half-step
    print("nbsteps {} and sign {}".format(nb,sign))
    for i in range(nb):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += sign
        # If we reach the end of the sequence
        # start again
        if (StepCounter==StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount-1
        # Wait before moving on
        time.sleep(WaitTime)

if __name__ == '__main__':
    try:
        while True:
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(TRIG, GPIO.LOW)

            # En este momento el sensor envía 8 pulsos ultrasónicos de 40kHz y coloca su pin ECHO en alto
            # Debemos detectar dicho evento para iniciar la medición del tiempo
            while True:
                pulso_inicio = time.time()
                if GPIO.input(ECHO) == GPIO.HIGH:
                    break

            while True:
                pulso_fin = time.time()
                if GPIO.input(ECHO) == GPIO.LOW:
                    break

            duracion = pulso_fin - pulso_inicio
            distancia = (34300 * duracion) / 2
            # Imprimimos resultado
            print( "Distancia: %.2f cm" % distancia)

            nbStepsPerRev=2048
            hasRun=False
            while not hasRun:
                if (distancia > 2):
                    steps(nbStepsPerRev) #adelante
                    time.sleep(1)
                else:
                    steps(-nbStepsPerRev) #pa atras
                    time.sleep(1)

    finally:
        GPIO.cleanup()
