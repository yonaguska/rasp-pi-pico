# rasp-pi-pico
Code and stuff related to the new Raspberry Pi Pico boards.

I am experimenting with MicroPython and Adafruit's CircuitPython,
hence the two folders. Each contains the appropriate pico UF2
file to initilize the board's Python. It also contains the
Python scripts I've been putzing with.

NOTES: 
  Use flash_nuke to clear the flash memory on the Pico.
  If you want you python script to run on boot, name it boot.py
  If your boot.py script loops forever, you may need to nuke
  the flash to stop that, but first you'll need to hold the
  reset button while connnecting the USB to halt everything,
  then drop the nuke file on the USB drive that represents the
  Pico board. You'll then need to drop the appropriate pico
  UF2 file on it to reestablish the board's Python.
