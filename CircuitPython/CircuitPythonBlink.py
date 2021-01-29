"""CircuitPython Essentials blink example"""
import time
import board
import digitalio

# LED setup.
ledPin = board.GP25
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

sleepmax = 2.5
sleeptime = 0.5
while True:
    print("CircuitPythonBlink sleeptime = {}".format(sleeptime))
    led.value = True
    time.sleep(sleeptime)
    led.value = False
    time.sleep(sleeptime)
    sleeptime += 0.5
    if sleeptime > sleepmax: sleeptime = 0.5
