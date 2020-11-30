import time
import board
import neopixel
import adafruit_hcsr04
import simpleio
ultrasonic = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)
neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

r = 0
b = 0
g = 0

while True:
    try:
        dist = ultrasonic.distance
        print(dist)
        if dist <= 20:
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 5, 20, 0, 255)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        else:
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 20, 35, 255, 0)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        neopixel.fill((int(r), int(g), int(b)))
        print(dist)
    except RuntimeError:
        print("Retrying!")
    time.sleep(.1)