#!/usr/bin/env python3
import time
from colorsys import hsv_to_rgb

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()

uh.set_brightness(0.5)

while True:
    #for x in range(17):
    #    for y in range(7):
    #        uh.set_pixel(x, y, 0, 255, 255)

    #uh.set_pixel(0, 0, 255, 0, 0)
    #uh.show()

    for x in range(7):
        # morning: 0-5
        # afternoon: 6-12
        # evening: 13-17
        start = 0
        end = 5
        
        #hue = (time.time() / 10.0)
        #r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
        
        r, g, b, = 0, 255, 255
        for y in range(start..end):
            uh.set_pixel(x, y, r, g, b)

    time.sleep(1.0 / 60)