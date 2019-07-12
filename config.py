#!/usr/bin/env python3

# author: Rishabh Ranjan

'''
Define and initialize global variables responsible for settings.
'''

# actual screen size in px
screen_width = 600
screen_height = 600

# computing model screen size
max_x = 100
max_y = 100

# conversion factors from model to actual co-ordinates
scale_x2px = screen_width / max_x
scale_y2px = screen_height / max_y

# wanted frames per second for drawing
fps = 100

# default particle properties
radius = 2 # px
thickness = 1 # px
saturation = 100 # 0 to 100
brightness = 60 # 0 to 100
alpha = 100 # 0 to 100
fade_alpha = 4 # 0 to 255, determines (with fps) the length of trail

# proportionality constant in inverse square law
# force is repulsive for +ve k
k_factor = 1

# merge particles that come closer than this (model units)
merge_threshold = 1

# conversion factor from model time to display (real) time (s)
scale_t2s = 5

