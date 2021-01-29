"""MicroPython Essentials blink example"""
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

sleepmax = 2.5
sleeptime = 0.5
led_onboard.value(0)
while True:
    print("MicroPythonBlink.py sleeptime = {}".format(sleeptime))
    led_onboard.toggle()
    utime.sleep(sleeptime)
    led_onboard.toggle()
    utime.sleep(sleeptime)
    sleeptime += 0.5
    if sleeptime > sleepmax: sleeptime = 0.5
