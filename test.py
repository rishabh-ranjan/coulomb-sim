import sys
import pygame
from Transform3D import Transform3D
from Render3D import Render3D
from vector import Vector

pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
fps = 20
center = Vector(600, 300, 0)
point = Vector(0, 0, 0)

tr = Transform3D()
rd = Render3D(1000, center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        tr.translate(Vector(-5, 0, 0))
    if keys[pygame.K_RIGHT]:
        tr.translate(Vector(5, 0, 0))
    if keys[pygame.K_UP]:
        tr.translate(Vector(0, -5, 0))
    if keys[pygame.K_DOWN]:
        tr.translate(Vector(0, 5, 0))
    if keys[pygame.K_j]:
        tr.translate(Vector(0, 0, 5))
    if keys[pygame.K_k]:
        tr.translate(Vector(0, 0, -5))
    if keys[pygame.K_f]:
        tr.rotate(0.01, Vector(0, 1, 0), center)
    if keys[pygame.K_d]:
        tr.rotate(-0.01, Vector(0, 1, 0), center)
    if keys[pygame.K_s]:
        tr.rotate(-0.01, Vector(1, 0, 0), center)
    if keys[pygame.K_a]:
        tr.rotate(0.01, Vector(1, 0, 0), center)

    screen.fill((0, 0, 0))
    for i in range(0, 400, 50):
        for j in range(0, 400, 50):
            for k in range(0, 400, 50):

                point = Vector(i, j, k)
                dpt = rd.render(tr.transform(point))
                pygame.draw.circle(screen, ((400 - k)/400 * 255, 0, 0), dpt, 2, 0)

    pygame.display.flip()
    clock.tick(fps)
