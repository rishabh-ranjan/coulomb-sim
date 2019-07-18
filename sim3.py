#!/usr/bin/env python3
# author: Rishabh Ranjan

import sys
import random
import time

import pygame

import config
import particle
from Transform3D import Transform3D
from Render3D import Render3D
from vector import Vector

def main():

    # ensures same list of random colors
    random.seed(1)
    particle.input_particles()

    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    # fade surface for trail effect
    #fade = pygame.Surface((config.screen_width, config.screen_height))
    #fade.set_alpha(config.fade_alpha)

    tr = Transform3D()
    rd = Render3D(1e9, Vector(config.screen_width/2, config.screen_height/2))
    lin = 2
    ang = 0.02
    zm = 1.1
    center = Vector(config.screen_width/2, config.screen_height/2, 0)

    # first frame
    particle.draw_state(screen)
    pygame.display.flip()
    last_draw_time = time.time()
    last_update_time = time.time()

    while True:

        #screen.blit(fade, (0, 0))
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            tr.translate(Vector(0, lin, 0))
        if keys[pygame.K_k]:
            tr.translate(Vector(0, -lin, 0))
        if keys[pygame.K_h]:
            tr.translate(Vector(-lin, 0, 0))
        if keys[pygame.K_l]:
            tr.translate(Vector(lin, 0, 0))
        if keys[pygame.K_x]:
            tr.rotate(ang, Vector(1, 0, 0), center)
        if keys[pygame.K_w]:
            tr.rotate(-ang, Vector(1, 0, 0), center)
        if keys[pygame.K_d]:
            tr.rotate(-ang, Vector(0, 1, 0), center)
        if keys[pygame.K_a]:
            tr.rotate(ang, Vector(0, 1, 0), center)
        if keys[pygame.K_f]:
            tr.rotate(ang, Vector(0, 0, 1), center)
        if keys[pygame.K_s]:
            tr.rotate(-ang, Vector(0, 0, 1), center)
        if keys[pygame.K_z]:
            tr.scale(zm, center)
        if keys[pygame.K_q]:
            tr.scale(1 / zm, center)

        # update state atleast once
        # but if more iterations are possible,
        # update and draw in such a way that fps is maintained
        while True:

            compute_begin = time.time()

            particle.handle_collisions()
            particle.compute_accs()

            now_time = time.time()
            dt = now_time - last_update_time
            particle.update_state(dt / config.scale_t2s)
            last_update_time = now_time

            compute_duration = time.time() - compute_begin

            if time.time() + compute_duration - last_draw_time > 1 / config.fps:
                break

        #particle.draw_state(screen)
        for p in particle.particles:
            dpt = rd.render(tr.transform(p.r * config.scale_x2px))
            pygame.draw.circle(screen, p.color, dpt, config.radius, config.thickness)

        pygame.display.flip()
        last_draw_time = time.time()

if __name__ == '__main__':
    main()
