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

while True:
    try:
        if GPIO.input(23):
            play(soundA)
        if GPIO.input(24):
            play(soundB)
        if GPIO.input(25):
            play(soundC)
        sleep(0.01)
    except KeyboardInterrupt:
        exit()
