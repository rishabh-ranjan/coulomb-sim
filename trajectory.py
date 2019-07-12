import sys
import random

import pygame

import config
import particle

max_update_disp = 0.001
updates_per_draw = int(1 / config.scale_x2px / max_update_disp)
if updates_per_draw == 0:
    updates_per_draw = 1

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        for i in range(updates_per_draw):

            particle.handle_collisions()
            particle.compute_accs()

            maxv = 0
            for p in particle.particles:
                maxv = max(maxv, p.v.norm())

            # glitches at lower values like 0.001
            # don't know why!
            def_dt = 0.005
            dt = def_dt if maxv == 0 else max_update_disp / maxv

            particle.update_state(dt)

        particle.draw_state(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
