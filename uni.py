#!/usr/bin/env python3
import time
from colorsys import hsv_to_rgb

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()

uh.set_brightness(0.5)

while True:
	for x in range(17):
		for y in range(7):
			uh.set_pixel(x, y, 0, 255, 255)

	uh.set_pixel(0, 0, 255, 0, 0)
	uh.show()
