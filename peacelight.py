#!/usr/bin/env python

'''
Scrollphat fill parameters
brightness: Brightness of pixels
x: Offset x: distance of the area from the left of the buffer
y: Offset y: distance of the area from the top of the buffer
width: Width of the area (default is 17)
height: Height of the area (default is 7)
'''

from datetime import datetime
from noise import pnoise1
from numpy import interp
import scrollphathd
import random
import time
import math

def peace():
  i = 1
  step = 1
  curr_hour = 0
  brightness = 0.0
  seed = random.uniform(0.1, 1.0)

	while True:
    now = datetime.datetime.now()
    current_time = now.time()
    start_time = datetime.time(18, 0)  # 6:00 PM
    end_time = datetime.time(23, 59, 59)  # Midnight

    if start_time <= current_time <= end_time:
      scrollphathd.clear()

      #brightness = interp(i, [-1.0, 1.0], [0.0, 1.0]) # map the brightness between 0 and 1
      b = interp(brightness, [-1.0, 1.0], [0.0, 1.0]) # map the brightness between 0 and 1
      scrollphathd.fill(b, 0, 0, i, scrollphathd.height)
      scrollphathd.show()

      # Sleep
      time.sleep( abs(0.45 + float( pnoise1( i * seed ) ) * 4.0) )

      # Control flow
      if (i >= scrollphathd.width or i <= 0):
        time.sleep( abs(5.25 + float(pnoise1( i * seed ) ) * 50.0 ) )
        if step == 1:
          step = -1
        else:
          step = 1
          i = i + step

          # Map brightness to hour of day, each hour
          hour = datetime.now().hour
          if (curr_hour <> hour):
            curr_hour = hour
            if (hour >= 11 and hour <= 14):
              brightness = 1.0 # brightest around noon
            elif (hour < 11 and hour > 0):
              brightness = brightness + 0.09 # taper up towards noon
            elif (hour > 14 and hour <= 23):
              brightness = brightness - 0.11 # taper down towards midnight
            else:
              brightness = -1.0 # erk, off

              # Ensure we max out at +=1.0, for interpolation later on
              if brightness > 1.0:
                brightness = 1.0
              elif brightness < -1.0:
                brightness = -1.0
              else:
                time.sleep(60)

def mapRange(value, inMin, inMax, outMin, outMax):
	return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

if __name__ == "__main__":
	peace()

