import pygame as pg
import math
import random
from vector import *
from entity import *
from fontman import *
from holder import *
from pgextras import *
from copy import copy
import pickle

screen_size = Vector2(1280, 720)
half_size = screen_size/2

# Setup
pg.init()
pg.font.init()

pg.display.set_caption("Paper Clicker")
window = pg.display.set_mode(screen_size.to_tuple())
clock = pg.time.Clock()

# objects
obj_paper = Entity(Vector2(300, half_size.y+100), 0, imgs["ToiletPaper"])
obj_shine = Entity(obj_paper.pos.copy(), 0, pg.transform.scale(imgs["Shine"], (500, 500)))
part_paper = Particles(
    fontmans["MBlack"].to_sur("+1", 0.5),
    4, 16, 10
)

# yea ik save and load functions are mess :3
def save_game():
    ups_d = []
    for k, v in ups.items():
        ups_d.append({
            "key"   : k,
            "level" : v.level,
            "cost"  : v.cost,
        })
    data = {
        "money" : paper,
        "ups" : ups_d
    }
    with open("save.bin", "wb") as f:
        pickle.dump(data, f)

def load_game():
    global paper, ups

    path = "save.bin"
    if not os.path.exists(path): return
    with open(path, "rb") as f:
        data = pickle.load(f)
    paper = data["money"]
    for ud in data["ups"]:
        u = ups[ud["key"]]
        u.level = ud["level"]
        u.cost = ud["cost"]


prev_paper = 0
paper = 0
paper_speed = 0

# timers
angle_timer = 0
cos_timer = 0
paper_timer = 0
sec_timer = 0
save_timer = 0


load_game()

running = True
while running:

    # Main Info
    delta_time = clock.get_time()/1000
    cos_timer += delta_time
    angle_timer += delta_time
    sec_timer += delta_time
    if cos_timer >= 11264: cos_timer -= 11264
    if angle_timer >= 360: angle_timer -= 360
    mouse_pos = Vector2().from_tuple(pg.mouse.get_pos())

    # Second timer logic
    sec_timer += delta_time
    if sec_timer >= 1:
        sec_timer -= 1
        paper_speed = max(0, paper - prev_paper)
        prev_paper = paper

    # Paper per second update
    if ups["second"].level > 1:

        paper_timer += delta_time * (ups["second"].level-1)
        if paper_timer >= 1:
            to_add = int(paper_timer)
            paper_timer -= to_add
            paper += to_add

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            save_game()
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:

            if obj_paper.hovered(mouse_pos.to_tuple()):

                paper += ups["click"].level
                part_paper.add_parts(1, mouse_pos, random.choice([-30, 30]), (-90, -20, 20))
            
            for k in ups_ents.keys():
                ent = ups_ents[k]

                if ent.hovered(mouse_pos.to_tuple()):
                    up = ups[k]

                    if up.can_buy(paper):
                        paper -= up.cost
                        up.upgrade()

                        if k=="click": part_paper.img = fontmans["MBlack"].to_sur(f"+{up.level}", font_size=0.5)
                        break
                
    
    window.fill(pg.Color(20, 20, 20))

    # FPS
    fps_ents = fontmans["MBlack"].convert(f"fps {int(clock.get_fps())}", Vector2(5, 5), Vector2(0, 0), 0.2)
    draw_many(window, fps_ents)

    # Shine
    obj_shine.angle = angle_timer*10
    obj_shine.auto_draw(window)

    # Paper Speed
    best_ents = fontmans["MBlack"].convert(f"{short_num(paper_speed)}/s", obj_paper.pos+Vector2(0, -290), font_size=0.5)
    for i in range(0, len(best_ents)):
        best_ents[i].img = flat_colorize(best_ents[i].img, pg.Color(75, 75, 75))
    cos_wave(best_ents, cos_timer*4, 0.1, 2)
    draw_many(window, best_ents)

    # Toilet paper
    obj_paper.pivot.y = 0.5-math.cos(cos_timer)/16
    obj_paper.angle = 3-math.cos(cos_timer/2)*6
    obj_paper.auto_draw(window)
    part_paper.process_all(delta_time, screen_size)
    part_paper.draw_all(window)

    # Score
    nums_ent = fontmans["MBlack"].convert(short_num(paper), obj_paper.pos+Vector2(0, -350), Vector2(0.5, 0.5))
    cos_wave(nums_ent, cos_timer*4, 0.1, 1)
    draw_many(window, nums_ent)

    # Upgrades
    for k in ups.keys():

        my_up = ups[k]
        ent = ups_ents[k]
        can_buy = my_up.can_buy(paper)

        if can_buy: ent.img = imgs["RichUpPlate"]
        else: ent.img = imgs["UpPlate"]

        # Label
        name_ents = fontmans["MBlack"].convert(my_up.name, ent.pos + Vector2(0, -30), font_size=0.5)
        cost_ents = fontmans["MBlack"].convert(f"${my_up.cost}", ent.pos + Vector2(190, 30), Vector2(1, 0.5), font_size=0.5)
        lvl_ents = fontmans["MBlack"].convert(f"{my_up.level} lvl", ent.pos + Vector2(-190, 30), Vector2(0, 0.5), font_size=0.5)

        ent.auto_draw(window)
        draw_many(window, cost_ents)
        draw_many(window, name_ents)
        draw_many(window, lvl_ents)
        

    # Finally
    clock.tick(60)
    pg.display.update()
    
pg.quit()