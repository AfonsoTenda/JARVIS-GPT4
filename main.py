import speech_recognition as sr
import pvporcupine
from unidecode import unidecode
import pyaudio
from time import sleep
import struct

from lib.ai import gpt
from lib.gpio import out, write
import lib.tts as tts
import lib.tuya as tuya
import lib.wiz as wiz

import data.pins as pins
import data.intent as intent

#Set all the pins to output
out(pins.g1_led)
out(pins.b2_led)
out(pins.b1_led)
out(pins.buzzer)

#Turn off all pins
write(pins.g1_led, 0)
write(pins.b1_led, 0)
write(pins.b2_led, 0)
write(pins.buzzer, 0)

#Turn on "SCRIPT RUNNING LED"
write(pins.g1_led, 1)

porcupine = None
pa = None
audio_stream = None

r = sr.Recognizer()

#Function which listens to commands
def listen_and_respond(source):
    #Alert the user that JARVIS is listening
    print("Listening...")
    write(pins.buzzer, 1)
    sleep(0.1)
    write(pins.buzzer, 0)
    write(pins.b2_led, 1)
    r.adjust_for_ambient_noise(source, duration = 0.5)
    while True:
        #STT Speech to Text
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en').lower()
            text = unidecode(text)
            print(f"You: {text}")
            write(pins.b2_led, 0)
            if not text:
                continue
            #All the programmable commands, if non of the commands is activated JARVIS will respond with a GPT4 answer 
            if text in intent.turn_on_ceiling_light:
                try:
                    wiz.turn_on()
                    tts.say("Lights on")
                except Exception as error:
                    tts("error " + str(error))
                wake_word()
            if text in intent.turn_off_ceiling_light:
                try:
                    wiz.turn_off()
                    tts.say("Lights off")
                except Exception as error:
                    tts("error " + str(error))
                wake_word()
            if text in intent.turn_on_desk_lamp:
                tuya.turn_on()
                tts.say("desk lamp on")
                wake_word()
            if text in intent.turn_off_desk_lamp :
                tuya.turn_off()
                tts.say("desk lamp off")
                wake_word()
            else:
                response = gpt(text)
                print(f"J.A.R.V.I.S: {response}")
                tts.say(response)
                wake_word()

            if not audio:
                wake_word()
        except sr.UnknownValueError:
            print("Silence found, listening for J.A.R.V.I.S again")
            write(pins.b2_led, 0)
            wake_word()
            break
            
        except sr.RequestError as e:
            print(f"ERROR: {e}")
            tts.say(f"ERROR: {e}")
            wake_word()
            break

#Function which listens for the wake word
def wake_word():
    porcupine = pvporcupine.create(keywords=["jarvis", "computer"], access_key="[Porcupine Key]")
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    print("Listening for J.A.R.V.I.S :")
    write(pins.b1_led, 1)
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("You called J.A.R.V.I.S")
            write(pins.b1_led, 0)
            with sr.Microphone() as source:
                listen_and_respond(source)

#Initiate Script
if __name__ == '__main__':
    tts.say("Jarvis at your service sir")
    wake_word()