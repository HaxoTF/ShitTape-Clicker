import pygame as pg
import math
from vector import *
from entity import *
from fontman import *
from holder import *

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
obj_paper = Entity(Vector2(300, half_size.y+100), 0, imgs["ToiletPaper"])
part_paper = Particles(
    obj_paper.pos + Vector2(-10, 70), 0, imgs["ToiletLeaf"], Vector2(0.5, 0.5),
    1, 1, 40
)

paper = 0
cos_timer = 0

running = True
while running:

    delta_time = clock.get_time()/1000
    cos_timer += delta_time
    if cos_timer >= 11264: cos_timer -= 11264
    
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()

            if obj_paper.hovered(mouse_pos):
                paper += 1
                part_paper.add_parts(1)
                
    
    window.fill(pg.Color(20, 20, 20))

    # Score
    nums_ent = fontmans["MBlack"].convert(f"${paper}", obj_paper.pos+Vector2(0, -300), Vector2(0.5, 0.5))
    for i in range(0, len(nums_ent)):
        nums_ent[i].pivot.y = math.cos((cos_timer+(i/4))*4)/8
    draw_many(window, nums_ent)

    # Toilet paper
    obj_paper.pivot.y = 0.5-math.cos(cos_timer)/16
    obj_paper.angle = 3-math.cos(cos_timer/2)*6
    obj_paper.auto_draw(window)
    part_paper.process_all(delta_time, screen_size)
    part_paper.draw_all(window)

    # Finally
    clock.tick(60)
    pg.display.update()
    
pg.quit()