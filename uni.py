#!/usr/bin/env python3
import time, datetime, noise, cmapy
from colorsys import hsv_to_rgb
from random import random, randint

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()

uh.set_brightness(0.1)

hour = start = end = num_rows = 0
max_width = 11

# Sunrise / sunset
#colours = [
#    [99, 37, 33],
#    [253,96,20],
#    [253,125,1],
#    [253,217,20],
#    [251,253,1],
#    [253,246,81],
#]

# https://pypi.org/project/colour/
# try list(red.range_to(lime, 5)) for sympathetic palettes

# Random colour palletes
# colour maps available: https://matplotlib.org/stable/tutorials/colors/colormaps.html
def set_colour_palette():
    colours = []
    for _ in range(8):
        colours.append( cmapy.color('viridis', random.randrange(0, 256, 8), rgb_order=True) )

# From https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

set_colour_palette()

while True:
    # Rotate through the palette
    colour = colours.pop(0)
    colours.append(colour)

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

    # v0.4.2
    # Off at night, quiet during the day, on in the evening
    pn = noise.pnoise2(random(), random())
    if hour in range(0):
        start, end = 0, 0
        uh.set_brightness(0)
        set_colour_palette()
    elif hour in range(1, 6):
        start, end = 0, 0
        uh.set_brightness(0.0 + pn)
    elif hour in range(6, 8):
        start, end = 0, 2
        uh.set_brightness(0.2 + pn)
    elif hour in range(8, 10):
        start, end = 0, 4
        uh.set_brightness(0.2 + pn)
    elif hour in range(10, 12):
        start, end = 2, 6
        uh.set_brightness(0.4 + pn)
    elif hour in range(12, 14):
        start, end = 3, 7
        uh.set_brightness(0.4 + pn)
    elif hour in range(16, 18):
        start, end = 4, 8
        uh.set_brightness(0.5 + pn)
    elif hour in range(18, 20):
        start, end = 6, 14
        uh.set_brightness(1.0)
    elif hour in range(20, 22):
        start, end = 8, 16
        uh.set_brightness(0.8 + pn)
    elif hour in range(22, 24):
        start, end = 16, 17
        uh.set_brightness(0.4 + pn)
    print(start, end, pn)

    for x in range(start, end):
        #hue = (time.time() / 10.0)
        #r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]

        r, g, b = colour

        for y in range(7):
            print(x, y)
            uh.set_pixel(x, y, r, g, b)

    uh.show()

    time.sleep(randint(2, 2048))
