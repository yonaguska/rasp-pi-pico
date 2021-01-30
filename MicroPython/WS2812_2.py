"""
    This is code derived from code in Raspberry Pi Org's book on the new Pico.
    I had to modify the driving of 'white' colors; the book's code didn't work
    correctly on my string, 'white' just turned the LEDs off.   
"""

import array, time
from machine import Pin
import rp2
from rp2 import PIO, StateMachine, asm_pio

# Configure the number of WS2812 LEDs.
NUM_LEDS   = 24 #8
MAX_LOOP   = 10
SLEEP_TIME = 50
MIN_RANGE  = 15
MAX_RANGE  = 31

# Here be dragons, I'll have to study up on use of PIO state machine use
@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)

def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    label("bitloop")
    out(x, 1)             .side(0)  [T3 - 1]
    jmp(not_x, "do_zero") .side(1)  [T1 - 1]
    jmp("bitloop")        .side(1)  [T2 - 1]
    label("do_zero")
    nop()                 .side(0)  [T2 - 1]
    
# Create the StateMachine with the ws2812 program, outputting on Pin(22)
sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(0))

# Start the StateMachine, it will wait for data on its FIFO
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

DIM_BLUE = 15
print("blue")
this_sleep = SLEEP_TIME
for j in range(0, MAX_LOOP):
    print("this_sleep {:>3}".format(this_sleep))
    # set the LEDs
    for i in range(0, NUM_LEDS):
        # we have a ring, turn on near and far LEDs
        near = i
        far  = NUM_LEDS - (i + 1)
        #print("near {:>2}  far {:>}".format(near, far))
        ar[near] = DIM_BLUE
        ar[far]  = DIM_BLUE
            
        sm.put(ar,8)
        time.sleep_ms(this_sleep)

    # clear the LEDs, in reverse order
    for i in range(0, NUM_LEDS/2):
        # we have a ring, turn off near and far LEDs
        near = (int(NUM_LEDS/2)) - (i + 1)
        far  = (int(NUM_LEDS/2)) + i
        #print("near {:>2}  far {:>}".format(near, far))
        ar[near] = 0
        ar[far]  = 0
            
        sm.put(ar,8)
        time.sleep_ms(this_sleep)
    
    this_sleep -= 5

# clear the LEDs, just to be sure
for i in range(NUM_LEDS):
    this = 0
    ar[i] = this
sm.put(ar,8)
