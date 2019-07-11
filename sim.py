#!/usr/bin/env python3

# author: Rishabh Ranjan

import sys
import math
import random
import time

import pygame

screen_width = 600
screen_height = 600
# compute with 100 * 100 size
# then scale to screen size
max_x = 100
max_y = 100
scale_x2px = screen_width / max_x
scale_y2px = screen_height / max_y

# less fps gives better accuracy but poorer display
fps = 24
particle_radius = 2 # px
particle_thickness = 1 # px
# particle colors
color_saturation = 100 # 0 to 100
color_brightness = 60 # 0 to 100
fade_alpha = 5 # 0 to 255, determines (with fps) the length of trail

# proportionality constant in inverse square law
# force is repulsive for +ve k
k = None # read from input file

# merge particles that come closer than this
merge_threshold = 1

class Particle:

    def __init__(self, m, q, x, y, vx, vy):
        self.m = m
        self.q = q
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.alive = True
        self.color = pygame.Color(0)
        self.color.hsla = (random.randint(0, 359), color_saturation, color_brightness, 100)

    def draw(self, screen):
        if not self.alive:
            return
        scr = (round(self.x * scale_x2px), round(self.y * scale_y2px))
        pygame.draw.circle(screen, self.color, scr, particle_radius, particle_thickness)

# list of particles
particles = []

# Initialize particles from input
# Format:
# one float representing k (described above)
# 5 space-separated floats (m, q, x, y, vx, vy) for each particle on a new line
# no newline at the end, just an EOF character: ctrl-D on *nix systems
def input_particles():
    global k
    k = float(input())
    while True:
        try:
            inp = map(float, input().split())
        except:
            break
        particles.append(Particle(*inp))

def handle_collisions():

    n = len(particles)
    for i in range(n):
        
        pi = particles[i]
        if not pi.alive:
            continue

        for j in range(n):

            pj = particles[j]
            if not pj.alive:
                continue
            if i == j:
                continue

            r2 = (pi.x - pj.x) ** 2 + (pi.y - pj.y) ** 2
            if r2 < merge_threshold ** 2:

                # merge into one particle
                pj.alive = False
                pi.x = (pi.m * pi.x + pj.m * pj.x) / (pi.m + pj.m)
                pi.y = (pi.m * pi.y + pj.m * pj.y) / (pi.m + pj.m)
                pi.vx = (pi.m * pi.vx + pj.m * pj.vx) / (pi.m + pj.m)
                pi.vy = (pi.m * pi.vy + pj.m * pj.vy) / (pi.m + pj.m)
                pi.m += pj.m
                pi.q += pj.q
                for k in range(3):
                    pi.color[k] = (pi.color[k] + pj.color[k]) // 2

def compute_accs():

    n = len(particles)

    for p in particles:
        p.ax = 0.0
        p.ay = 0.0

    for i in range(n):

        pi = particles[i]
        if not pi.alive:
            continue

        for j in range(n):
            if i == j:
                continue;

            pj = particles[j]
            if not pj.alive:
                continue

            r = math.sqrt( (pi.x - pj.x) ** 2 + (pi.y - pj.y) ** 2 )                
            a = (k * pi.q * pj.q) / (r * r * pi.m)
            pi.ax += a * (pi.x - pj.x) / r
            pi.ay += a * (pi.y - pj.y) / r

def update_state(dt):

    for p in particles:
        p.vx += p.ax * dt
        p.vy += p.ay * dt
        p.x += p.vx * dt
        p.y += p.vy * dt

def draw_state(screen):
    
    for p in particles:
        p.draw(screen)

def main():

    # ensures same list of random colors
    random.seed(1)
    input_particles()

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    fade = pygame.Surface((screen_width, screen_height))
    fade.set_alpha(fade_alpha)

    # first frame
    draw_state(screen)
    pygame.display.flip()
    old_time = time.time()

    while True:
        screen.blit(fade, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        prev_time = old_time
        while time.time() - old_time < 1 / fps:
            now_time = time.time()
            handle_collisions()
            compute_accs()
            dt = now_time - prev_time
            update_state(dt)
            prev_time = now_time

        draw_state(screen)
        pygame.display.flip()
        old_time = time.time()

if __name__ == '__main__':
    main()
