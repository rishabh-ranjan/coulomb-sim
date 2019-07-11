import sys
import math
import random

import pygame

import config
import vector
from vector import Vector

class Particle:

    def __init__(self, m, q, r, v):
        self.m = m
        self.q = q
        self.r = r
        self.v = v

        self.a = None
        self.alive = True
        self.color = pygame.Color(0)
        hue = random.randint(0, 359)
        self.color.hsla = (hue, config.saturation, config.brightness, config.alpha)
        self.radius = config.radius
        self.thickness = config.thickness
        
    def draw(self, screen):
        if not self.alive:
            return

        pos = (round(self.r.x * config.scale_x2px), round(self.r.y * config.scale_y2px))
        pygame.draw.circle(screen, self.color, pos, self.radius, self.thickness)

# list of particles
particles = []

def input_particles():
    '''
    initialize particles from input
    first line a float representing k_factor
    for each particle 3 lines of floats:
    m q
    r.x r.y r.z
    v.x v.y v.z
    '''

    config.k_factor = float(input().strip())

    while True:
        try:
            m, q = map(float, input().split())
            r = Vector(*map(float, input().split()))
            v = Vector(*map(float, input().split()))
        except (EOFError, ValueError):
            break
        
        particles.append(Particle(m, q, r, v))

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

            d = vector.dist(pi.r, pj.r)
            if d < config.merge_threshold:

                # merge into one particle
                pj.alive = False
                pi.r = (pi.r * pi.m + pj.r * pj.m) / (pi.m + pj.m)
                pi.v = (pi.v * pi.m + pj.v * pj.m) / (pi.m + pj.m)
                pi.m += pj.m
                pi.q += pj.q
                for k in range(3):
                    pi.color[k] = (pi.color[k] + pj.color[k]) // 2

def compute_accs():

    n = len(particles)

    for p in particles:
        p.a = Vector()

    for i in range(n):

        pi = particles[i]
        if not pi.alive:
            continue

        for j in range(n):
            if i == j:
                continue

            pj = particles[j]
            if not pj.alive:
                continue

            d = vector.dist(pi.r, pj.r)
            a = (config.k_factor * pi.q * pj.q) / (d * d * pi.m)
            pi.a += (pi.r - pj.r) * (a / d)

def update_state(dt):

    for p in particles:
        if not p.alive:
            continue
        
        p.v += p.a * dt
        p.r += p.v * dt

def draw_state(screen):

    for p in particles:
        p.draw(screen)
