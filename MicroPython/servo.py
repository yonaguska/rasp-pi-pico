# Example using PWM to drive a servo.

import time
from machine import Pin, PWM


# Construct PWM object, for a SG90 servo
servo = PWM(Pin(15))
# Set the PWM frequency.
servo.freq(50)

# play with the servo
start = 2500
end   = 1700 * 5
step  = 1
duty  = start
sleeptime = 1
print('duty {:6d}  start {}  end {}  step {}'.format(duty, start, end, step))
while True:
    #print('duty {:6d}  step {}'.format(duty, step))
    servo.duty_u16(duty)
    time.sleep_ms(sleeptime)
    #
    if step > 0: # rotate counterclockwise
        if duty < end:
            duty += step
        else:
            step = -(step)        
    else:        # rotate clockwise
        if duty > start:
            duty += step
        else:
            step = -(step)        
