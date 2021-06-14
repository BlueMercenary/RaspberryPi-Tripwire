# RaspberryPi-Tripwire
A phototransistor and distance sensor "tripwire" security system based on the raspberry pi.

This is a project meant to be mounted to a door-frame and to have a light shining from the other side of the door onto the phototransistor.

This is so that if the light can be cut off by someone walking through the door.
The distance sensor is a redundancy to detect something coming through the door.

When it detects something, it will briefly run the piezo buzzer and RGB LED.
It will also scream using text to speech if you connect a speaker to its headphone jack. 

This is done using gpiozero, pianalog, multiprocessing, pyttsx3, time, math 
*pyttsx3 requires espeak to be installed if it isn't already

The distance sensor it set to detect movement at any distance lower than 1 meter

The RGB LED flashes from red to green to blue

