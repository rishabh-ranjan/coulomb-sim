import sys
import math
import random

import pygame
import pygame.locals

screen_width = 600
screen_height = 600
# compute with 100 * 100 size
# then scale to screen size
max_x = 100
max_y = 100
scale_x2px = screen_width / max_x
scale_y2px = screen_height / max_y

fps = 24
particle_radius = 3 # px
particle_thickness = 1 # px
color_saturation = 50 # 0 to 100
color_brightness = 50 # 0 to 100

# proportionality constant in inverse square law
# force is repulsive for +ve k
k = None # read from input file

class Particle:

    def __init__(self, m, q, x, y, vx, vy):
        self.m = m
        self.q = q
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.color = pygame.Color(0)
        self.color.hsla = (random.randint(0, 359), color_saturation, color_brightness, 100)

    def draw(self, screen):
        scr = (int(self.x * scale_x2px), int(self.y * scale_y2px))
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
        except (EOFError, ValueError):
            break
        particles.append(Particle(*inp))

def compute_accs():

    n = len(particles)
    for i in range(n):
        pi = particles[i]
        pi.ax = 0.0
        pi.ay = 0.0

        for j in range(n):
            if (i == j):
                continue;

            pj = particles[j]
            r = math.sqrt( (pi.x - pj.x) ** 2 + (pi.y - pj.y) ** 2 )
            a = (k * pi.q * pj.q) / (r * r * pi.m)
            pi.ax += a * (pi.x - pj.x) / r
            pi.ay += a * (pi.y - pj.y) / r

def update_state():

    dt = 1 / fps

    for p in particles:
        p.vx += p.ax * dt
        p.vy += p.ay * dt
        p.x += p.vx * dt
        p.y += p.vy * dt

def draw_state(screen):
    
    for p in particles:
        p.draw(screen)

def main():

    # ensures same set of random colors
    random.seed(0)
    input_particles()

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.locals.RESIZABLE)
    clock = pygame.time.Clock()

    while True:
        #screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        compute_accs()
        update_state()
        draw_state(screen)

        pygame.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    main()
