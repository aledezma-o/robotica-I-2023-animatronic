import speech_recognition as sr
import serial
# import RPi.GPIO as GPIO
from gtts import gTTS
import os
import random

# Configurar comunicación con Arduino

#arduino = serial.Serial('/dev/ttyACM0', 9600)

# Configurar micrófono
mic = sr.Recognizer()

# Configurar pin PWM para controlar el servo
servo_pin = 9
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servo_pin, GPIO.OUT)
# pwm = GPIO.PWM(servo_pin, 50)
# pwm.start(0)

# Lista de frases inspiracionales
inspirational_quotes = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No importa lo lento que vayas, siempre y cuando no te detengas.",
    "Si puedes soñarlo, puedes hacerlo.",
    "El fracaso es solo la oportunidad de comenzar de nuevo, pero de manera más inteligente."
]

# Función para mover el servo a una posición determinada
# def move_servo(position):
#     duty = position / 18 + 2
#     pwm.ChangeDutyCycle(duty)

def play_text(text):
    tts = gTTS(text=text, lang='es')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def respond_to_hello():
    quote = random.choice(inspirational_quotes)
    response = f"Buenos días! Aquí tienes una frase inspiracional para hoy: {quote}"
    print(response)
    play_text(response)

while True:
    #data = arduino.readline().decode().strip()
    #if data == "button_pressed":
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = mic.listen(source)
            
        try:
            command = mic.recognize_google(audio, language="es-ES")
            print("Comando de voz: ", command)
            
            if command.lower() == "hola":
                respond_to_hello()
                
            # Aquí puedes agregar las acciones correspondientes a otros comandos de voz
            
            # elif command.lower() == "mover servo 30 grados":
            #     move_servo(30)
                
        except sr.UnknownValueError:
            print("No se entendió el comando")
        except sr.RequestError as e:
            print("Error al obtener resultados: {0}".format(e))