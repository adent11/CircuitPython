import time
import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

touch_pad1 = board.A0
switch = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A1
button = touchio.TouchIn(touch_pad2)

change = 1
value = 0
switchFlipped = False
buttonPressed = False

lcd.print("Hello, Engineer!")
while True:

    if switch.value and not switchFlipped:
        change = change*-1
        switchFlipped = True
    if not switch.value:
        switchFlipped = False
    if button.value and not buttonPressed:
        value = value + change
        buttonPressed = True
    if not button.value:
        buttonPressed = False
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print('Increment ' + str(change))
    lcd.set_cursor_pos(1,0)
    lcd.print('Value ' + str(value))
    print('Incrementing by ' + str(change))
    print('Value is ' + str(value))
    time.sleep(.1)
