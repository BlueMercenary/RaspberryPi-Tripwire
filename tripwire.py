from gpiozero import DigitalOutputDevice, DistanceSensor, RGBLED
import time, math
from PiAnalog import *
from colorzero import Color
import multiprocessing
import pyttsx3

#Variables and pins
sensor = DistanceSensor(echo=6, trigger=17)
pin1 = DigitalOutputDevice(24)
pin2 = DigitalOutputDevice(25)
led = RGBLED(13, 19, 26)
p = PiAnalog()
L = 0
D = 0
engine = pyttsx3.init()


# Rgb led function
def rgb():
    led.color = Color('red')
    time.sleep(1)
    led.color = Color('green')
    time.sleep(1)
    led.color = Color('blue')
    time.sleep(1)
    led.color = Color('black')

#Buzzer function
def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0, cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.on()
        delay(p2)

# delay function
def delay(p):
    t0 = time.time()
    while time.time() < t0 + p:
        pass

# Phototransistor
multiplier = 20000 # increase to make more sensitive


def light_from_r(R):
    light = 1/math.sqrt(R) * multiplier
    if light > 200:
        light = 200
    # Sqareroot the reading to compress the range
    return light

# Get phototransistor reading
def update_reading():
    global L
    L = int(light_from_r(p.read_resistance()))
    print(int(light_from_r(p.read_resistance())))

# distance sensor reading
def distances():
    global D
    D = int(sensor.distance * 100)
    print('Distance: ', int(sensor.distance * 100))

# Text to speech
def tts():
    engine.say("INTRUDER! INTRUDER! INTRUDER! INTRUDER!")
    engine.runAndWait()

# Run Code
while True:
    update_reading()
    distances()
    if L <= 150 or D < 100:
        reading = p.analog_read() # 1000 to 5000 ish for indoors
        f = reading * 2
        buzzer = multiprocessing.Process(target = buzz(f, 1))
        light1 = multiprocessing.Process(target = rgb())
        speeeee = multiprocessing.Process(target = tts())
        buzzer.start()
        light1.start()
        speeeee.start()
