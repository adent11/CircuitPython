import time
import board
import pulseio
import touchio
import servo

angle = 180

touch_pad1 = board.A0
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A1
touch2 = touchio.TouchIn(touch_pad2)

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    if touch1.value and not touch2.value and angle < 180:
        angle += 1
    if touch2.value and not touch1.value and angle > 0:
        angle -= 1
    print(angle)
    my_servo.angle = angle
    time.sleep(.01)