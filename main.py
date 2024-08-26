import pygame as pg
import images as img
import math
from vector import *
from entity import *

screen_size = Vector2(1280, 720)
half_size = screen_size/2

pg.init()
window = pg.display.set_mode(screen_size.to_tuple())

# objects
obj_paper = Entity(half_size.copy(), 0, img.toilet_paper)

running = True
while running:
    
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    window.fill(pg.Color(50, 100, 255))
    obj_paper.auto_draw(window)

    pg.display.update()
    
pg.quit()