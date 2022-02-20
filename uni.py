#!/usr/bin/env python3
import time, datetime
from colorsys import hsv_to_rgb

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()

uh.set_brightness(0.1)

hour = start = end = num_rows = 0
max_width = 11

# From https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

while True:
    uh.clear()

    # morning: 0-5
    # afternoon: 6-12
    # evening: 13-17
    hour = datetime.datetime.now().hour

    # attempting to map time to position, failing for now...
    #h = datetime.datetime.now().hour
    #hour = mapRange(h, 0, 23, 0, 17)
    #print(h)
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
    #if num_rows >= 10:
    #    start = start + 1
    #    end = end + 1
    #    if start > 17:
    #        start, end = 0, 0
    #else:
    #    end = end + 1
    #    num_rows = num_rows + 1
    #print(start, end, num_rows)
    #print('-----s, e, n_r')

    # v0.4
    if hour in range(0, 2):
        start, end = 0, 2
        uh.set_brightness(0.1)
    elif hour in range(2, 4):
        start, end = 1, 3
        uh.set_brightness(0.2)
    elif hour in range(4, 6):
        start, end = 2, 4
        uh.set_brightness(0.3)
    elif hour in range(6, 8):
        start, end = 3, 5
        uh.set_brightness(0.3)
    elif hour in range(8, 10):
        start, end = 4, 8
        uh.set_brightness(0.5)
    elif hour in range(10, 12):
        start, end = 6, 10
        uh.set_brightness(0.7)
    elif hour in range(12, 14):
        start, end = 5, 10
        uh.set_brightness(1.0)
    elif hour in range(16, 18):
        start, end = 6, 12
        uh.set_brightness(0.7)
    elif hour in range(18, 20):
        start, end = 9, 13
        uh.set_brightness(0.4)
    elif hour in range(20, 22):
        start, end = 13, 15
        uh.set_brightness(0.2)
    elif hour in range(22, 24):
        start, end = 16, 17
        uh.set_brightness(0.1)
    print(start, end)


    for x in range(start, end):
        hue = (time.time() / 1000.0)
        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]

        for y in range(7):
            print(x, y)
            uh.set_pixel(x, y, r, g, b)

    uh.show()

    time.sleep(5040)
