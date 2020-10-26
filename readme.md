# CircuitPython

This is my repository for the introductory CircuitPython assignments.

---
## Table of Contents
* [Table of Contents](#Table-of-Contents)
* [Hello CircuitPython](#Hello-CircuitPython)

---

## Hello CircuitPython

### Description

In this assignment I got the Metro M0 Express board working, and coded a simple fade between green and blue with the built in LED.

### Code

``` python
import board
import neopixel
import time
x = 0
change = 1

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    if x > 254:
        up = -1
    if x < 1:
        up = 1
    x += up
    dot.fill((0, -x+255, x))
    time.sleep(.1)
    print("Green Level: ", -x+255)
    print("Blue Level:", x)
```


### Reflection
At first I wasn't able to control the LED, but after updating the board [here](https://circuitpython.org/board/metro_m0_express/), and getting the correct library [here](https://circuitpython.org/libraries), it worked fine. It is very convenient that the Metro Express has a built in LED.
