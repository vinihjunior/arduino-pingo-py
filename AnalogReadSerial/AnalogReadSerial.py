"""
Implementation of a Serial Monitor for reading the value of a potentiometer.

"""

import pingo
import time

board = pingo.detect.MyBoard()

sensorValue = board.pins['A0']
sensorValue.mode = pingo.IN

while True:
	print(sensorValue.value) #Serial Monitor 
	time.sleep(0.05)
