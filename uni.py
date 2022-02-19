#!/usr/bin/env python3
import time, datetime
from colorsys import hsv_to_rgb

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()

uh.set_brightness(0.1)

hour = start = end = num_rows = 0

# From https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

while True:
    uh.clear()

    # morning: 0-5
    # afternoon: 6-12
    # evening: 13-17
    h = datetime.datetime.now().hour

    # attempting to map time to position, failing for now...
    hour = mapRange(h, 0, 23, 0, 17)
    print(h)
    print(hour)
    print('---h, hour')

    # v0.1
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


    # v0.2
    #if hour in range(0, 8):
    #    start, end = 0, 7
    #    uh.set_brightness(0.3)
    #elif hour in range(8, 16):
    #    start, end = 4, 13
    #    uh.set_brightness(0.7)
    #elif hour in range(16, 24):
    #    start, end = 9, 16
    #    uh.set_brightness(0.1)
    #print(start, end)


    # v0.3 (update every 1.4 hours/5040 seconds)
    if num_rows >= 10:
        start = start + 1
        end = end + 1
        if start > 17:
            start, end = 0, 0
    else:
        end = end + 1
        num_rows = num_rows + 1
    print(start, end, num_rows)
    print('-----s, e, n_r')
    
    for x in range(start, end):
        hue = (time.time() / 1000.0)
        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]

        for y in range(7):
            print(x, y)
            uh.set_pixel(x, y, r, g, b)

    uh.show()

    time.sleep(5040)
