#!/usr/bin/env python3
import time, datetime
from colorsys import hsv_to_rgb

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()

uh.set_brightness(0.1)

hour = 0

while True:
    uh.clear()

    # morning: 0-5
    # afternoon: 6-12
    # evening: 13-17
    hour = datetime.datetime.now().hour

    print(hour)
    print('---hour')

    #if hour in range(6, 12):
    #    start, end = 0, 5
    #    uh.set_brightness(0.1)
    #elif hour in range(12, 18):
    #    start, end = 6, 12
    #    uh.set_brightness(0.5)
    #elif hour in range(18, 20):
    #    start, end = 11, 16
    #elif hour in range(20, 23):
    #    start, end = 13, 16
    #    uh.set_brightness(0.1)
    #else:
    #    start, end = 0, 1
    #    uh.set_brightness(0.0)

    if hour in range(0, 8):
        start, end = 0, 7
        uh.set_brightness(0.3)
    elif hour in range(8, 16):
        start, end = 4, 13
        uh.set_brightness(0.7)
    elif hour in range(16, 24):
        start, end = 9, 16
        uh.set_brightness(0.1)
    print(start, end)

    for x in range(start, end):
        hue = (time.time() / 1000.0)
        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]

        for y in range(7):
            print(x, y)
            uh.set_pixel(x, y, r, g, b)

    uh.show()

    time.sleep(10)
