import sys
import random
import time

import pygame

import config
import vector
from vector import Vector
import particle

def main():

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
    last_draw_time = time.time()
    last_update_time = time.time()

    while True:

        screen.blit(fade, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

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

        particle.draw_state(screen)
        pygame.display.flip()
        last_draw_time = time.time()

if __name__ == '__main__':
    main()
