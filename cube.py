import sys
import pygame
from Transform3D import Transform3D
from Render3D import Render3D
from vector import Vector

pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
fps = 100
lin = 2
ang = 0.02
tr = Transform3D()
w, h = screen.get_size()
rd = Render3D(1e9, Vector(w/2, h/2))

center = Vector(w/2, h/2, 50)

cube_pts = [
        Vector(0, 0, 0),
        Vector(0, 1, 0),
        Vector(1, 0, 0),
        Vector(1, 1, 0),
        Vector(0, 0, 1),
        Vector(0, 1, 1),
        Vector(1, 0, 1),
        Vector(1, 1, 1) ]
cube_lns = [
        (0, 1), 
        (0, 2), 
        (1, 3),
        (2, 3),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7) ]

tr.scale(100)
tr.translate(Vector(w/2 - 50, h/2 - 50))

while True:
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

    screen.fill((0, 0, 0))
    d_pts = []
    for p in cube_pts:
        d_pts.append(rd.render(tr.transform(p)))
    for s, e in cube_lns:
        pygame.draw.line(screen, (255, 0, 0), d_pts[s], d_pts[e])

    pygame.display.flip()
    clock.tick(fps)

