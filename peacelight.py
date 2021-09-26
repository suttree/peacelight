#!/usr/bin/env python

import scrollphathd

def peace(brightness-1.0):
    scrollphathd.fill(brightness, x=0, y=0, width=0, height=scrollphathd.DISPLAY_HEIGHT)


while True:
    # FILL FROM WIDTH TO 0, FULL HEIGHT
    # SLEEP
    time.sleep(0.001)
    # FILL FROM WIDTH-1 TO 0, FULL HEIGHT 
    # SHOW THE BUFFER
    scrollphathd.show()


    # DO THE SAME BUT LOWERING THE BRIGHTNESS TOO

'''
Parameters
brightness: Brightness of pixels
x: Offset x: distance of the area from the left of the buffer
y: Offset y: distance of the area from the top of the buffer
width: Width of the area (default is 17)
height: Height of the area (default is 7)
'''
