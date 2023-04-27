from google.cloud import speech_v1 as speech
from google.cloud.speech_v1 import types
import io
import pyaudio

client = speech.SpeechClient.from_service_account_json('tranquil-door-385000-e600ec5b3f29.json')

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

config = speech.RecognitionConfig(
    encoding=types.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code='en-US'
)

section = 0
while True:
    frames = []
    print("Section: ", section)
    for i in range(0, int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    audio = speech.RecognitionAudio(content=b''.join(frames))
    
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    section += 1

