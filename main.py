import pygame as pg
import images as img
import math
from vector import *
from entity import *
from nums import *

screen_size = Vector2(1280, 720)
half_size = screen_size/2

# Setup
pg.init()
pg.font.init()

main_font = pg.font.SysFont("Consolas", 32)

pg.display.set_caption("Paper Clicker")
window = pg.display.set_mode(screen_size.to_tuple())
clock = pg.time.Clock()

# objects
obj_paper = Entity(half_size.copy(), 0, img.toilet_paper)
cos_timer = 0

paper = 0
paper_numman = NumMan().load("./images/nums")

running = True
while running:

    delta_time = clock.get_time()/1000
    cos_timer += delta_time
    if cos_timer >= 44: cos_timer -= 44
    
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()

            if obj_paper.hovered(mouse_pos):
                paper += 1
    
    window.fill(pg.Color(50, 100, 255))

    window.blit(paper_numman.render(paper), (10, 10))
    obj_paper.pivot.y = 0.5-math.cos(cos_timer*2)/10
    obj_paper.angle = 3-math.cos(cos_timer)*6
    obj_paper.auto_draw(window)

    # Finally
    clock.tick(60)
    pg.display.update()
    
pg.quit()