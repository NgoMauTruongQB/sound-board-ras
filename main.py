from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
from time import sleep
from sys import exit
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

# Lấy đường dẫn thư mục hiện tại của script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Tạo các đường dẫn tuyệt đối đến các file âm thanh
soundA = AudioSegment.from_file(os.path.join(script_dir, "sound1.mp3"))
soundB = AudioSegment.from_file(os.path.join(script_dir, "sound2.mp3"))
soundC = AudioSegment.from_file(os.path.join(script_dir, "sound3.mp3"))

print("Soundboard Ready.")

current_playing = None

while True:
    try:
        if GPIO.input(23):
            if current_playing != soundA:
                if current_playing:
                    play(soundA)
                    current_playing = soundA
        if GPIO.input(24):
            if current_playing != soundB:
                if current_playing:
                    play(soundB)
                    current_playing = soundB
        if GPIO.input(25):
            if current_playing != soundC:
                if current_playing:
                    play(soundC)
                    current_playing = soundC
        sleep(0.01)
    except KeyboardInterrupt:
        exit()
