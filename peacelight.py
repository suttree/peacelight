#!/usr/bin/env python

'''
Parameters
brightness: Brightness of pixels
x: Offset x: distance of the area from the left of the buffer
y: Offset y: distance of the area from the top of the buffer
width: Width of the area (default is 17)
height: Height of the area (default is 7)
'''

from noise import pnoise1
from numpy import interp
import scrollphathd
import time
import math

def peace():
	i = 1
	step = 1
	brightness = 0

	while True:
		scrollphathd.clear()

		brightness = interp(i, [-1, 1], [0,1]) # map the brightness between 0 and 1
		scrollphathd.fill(brightness, 0, 0, i, scrollphathd.height)

		scrollphathd.show()

		# SLEEP
		time.sleep( 0.75 + float(pnoise1(i)) * 5.0 )

		# CONTROL FLOW
		if (i >= scrollphathd.width or i <= 0):
			time.sleep(2.25 + float(pnoise1(i)) * 10.0 )
			if step == 1:
				step = -1
			else:
				step = 1

		i = i + step
		

def mapRange(value, inMin, inMax, outMin, outMax):
	return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

if __name__ == "__main__":
	peace()
