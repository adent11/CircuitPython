import time
import math
import board
import touchio
import digitalio
import adafruit_bus_device

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
lcd.print("Interrupt Count:")

photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP

lastTime = time.monotonic()

isInterrupted = True
counter = 0

while True:
    if time.monotonic() > lastTime + 4:
        lastTime = time.monotonic()
        lcd.set_cursor_pos(1, 0)
        lcd.print('         ')
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(counter))
    if photoPin.value and not isInterrupted:
        counter += 1
        isInterrupted = True
    if not photoPin.value:
        isInterrupted = False