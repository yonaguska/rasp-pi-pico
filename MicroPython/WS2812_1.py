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
NUM_LEDS = 8
MAX_LOOP   = 10
SLEEP_TIME = 10
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

for k in range(0, MAX_LOOP):
    print("blue")
    for j in range(MIN_RANGE, MAX_RANGE):
        for i in range(NUM_LEDS):
            ar[i] = j
        sm.put(ar,8)
        time.sleep_ms(SLEEP_TIME)
    
    print("red")
    for j in range(MIN_RANGE, MAX_RANGE):
        for i in range(NUM_LEDS):
            ar[i] = j<<8
        sm.put(ar,8)
        time.sleep_ms(SLEEP_TIME)
    
    print("green")
    for j in range(MIN_RANGE, MAX_RANGE):
        for i in range(NUM_LEDS):
            ar[i] = j<<16
        sm.put(ar,8)
        time.sleep_ms(SLEEP_TIME)
    
    print("white")
    for j in range(MIN_RANGE, MAX_RANGE):
        for i in range(NUM_LEDS):
            g = j<<16
            r = j<<8
            b = j
            ar[i] = r + g + b
        sm.put(ar,8)
        time.sleep_ms(SLEEP_TIME)
    SLEEP_TIME -= 1

# clear the LEDs
for i in range(NUM_LEDS):
    this = 0
    ar[i] = this
sm.put(ar,8)
