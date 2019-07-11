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
    fade = pygame.Surface((config.screen_width, config.screen_height))
    fade.set_alpha(config.fade_alpha)

    # first frame
    particle.draw_state(screen)
    pygame.display.flip()
    old_time = time.time()

    while True:
        screen.blit(fade, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        prev_time = old_time
        while time.time() - old_time < 1 / config.fps:

            now_time = time.time()

            particle.handle_collisions()
            particle.compute_accs()

            dt = now_time - prev_time
            particle.update_state(dt)

            prev_time = now_time

        particle.draw_state(screen)
        pygame.display.flip()
        old_time = time.time()

if __name__ == '__main__':
    main()
