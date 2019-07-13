#!/usr/bin/env python3
# author: Rishabh Ranjan

import sys
import random

import pygame

import config
import particle

max_update_disp = 0.01
updates_per_draw = int(1 / config.scale_x2px / max_update_disp)
if updates_per_draw == 0:
    updates_per_draw = 1
max_update_vel = 0.01 # used in very rare cases when all velocities are zero

def main():
    '''
    Create more accurate trajectories
    without caring for sync with real time.
    '''

    # ensures same list of random colors
    random.seed(1)
    particle.input_particles()

    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    # fade surface for trail effect
    fade = pygame.Surface((config.screen_width, config.screen_height))
    fade.set_alpha(config.fade_alpha)

    # first frame
    particle.draw_state(screen)
    pygame.display.flip()

    while True:

        screen.blit(fade, (0, 0))

        for i in range(updates_per_draw):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            particle.handle_collisions()
            particle.compute_accs()

            maxv = 0
            for p in particle.particles:
                maxv = max(maxv, p.v.norm())

            if maxv == 0:
                maxa = 0
                for p in particle.particles:
                    maxa = max(maxa, p.a.norm())

                if maxa == 0:
                    print('All particles will remain stationary.')
                    print('Terminating simulation!')
                    sys.exit(0)
                else:
                    dt = max_update_vel / maxa

            else:
                dt = max_update_disp / maxv

            particle.update_state(dt)

        particle.draw_state(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
