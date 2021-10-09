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
    i = 0

    while True:
        # RESET THE COUNTER IF NEEDED
        if (i >= scrollphathd.width):
            i = 0

        scrollphathd.fill(0.5, 0, 0, i, scrollphathd.height)
        scrollphathd.show()

        # SLEEP
        time.sleep(1)

        print i
        print "----"

        i = i+1


if __name__ == "__main__":
    peace()
