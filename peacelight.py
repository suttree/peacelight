#!/usr/bin/env python

'''
Parameters
brightness: Brightness of pixels
x: Offset x: distance of the area from the left of the buffer
y: Offset y: distance of the area from the top of the buffer
width: Width of the area (default is 17)
height: Height of the area (default is 7)
'''

import scrollphathd
import time
import math

def peace():
	i = 1
	step = 1

	while True:
		scrollphathd.clear()
		scrollphathd.fill(0.5, 0, 0, i, scrollphathd.height)
		scrollphathd.show()

		# SLEEP
		time.sleep(0.5)

		print i
		print "----"

		# CONTROL FLOW
		if (i >= scrollphathd.width or i <= 0):
			if step == 1:
				step = -1
			else:
				step = 1

		i = i + step


if __name__ == "__main__":
	peace()
