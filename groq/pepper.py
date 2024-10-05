import qi
import sys
# import naoqi


# Creamos un objeto de conexión
session = qi.Session()

try:
    # Conectamos a la robot Pepper
    session.connect("tcp://127.0.0.1:9552")
except qi.Failure as e:
    print("Cannot connect to the robot : ", e)
    sys.exit(1)

# Accedemos al servicio de voz del robot
speech = session.service("ALTextToSpeech")

# Decimos "Hola"
speech.say("Hola")

# Cerramos la conexión
session.close()