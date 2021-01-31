# Example using PWM to fade an LED.

import time
from machine import Pin, PWM


# Construct PWM object, with onboard LED on Pin(25).
pwm = PWM(Pin(25))
# Construct PWM object, with offboard LED on Pin(1).
pwm2 = PWM(Pin(1))

# Set the PWM frequency.
pwm.freq(1000)
pwm2.freq(1000)

# Fade the LED in and out a few times.
duty = 0
direction = 1
for _ in range(8 * 256):
    #print('_ {}'.format(_))
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    pwm2.duty_u16(duty * duty)
    time.sleep(0.001)
