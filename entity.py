import pygame as pg
from vector import *

class Entity:
    def __init__(self, pos:Vector2=Vector2(0, 0), angle=0, img:pg.Surface=None, pivot:Vector2=Vector2(0.5, 0.5)):
        self.pos :Vector2 = pos
        self.angle :float = angle
        self.img :pg.Surface = img
        self.pivot :Vector2 = pivot
    
    def auto_draw(self, window:pg.Surface):

        if self.angle == 0: img = self.img
        else: img = pg.transform.rotate(self.img, self.angle)

        draw_pos = self.pos - Vector2(img.get_width(), img.get_height()) * self.pivot
        window.blit(img, draw_pos.to_tuple())
    
    def hovered(self, mouse_pos:Vector2|tuple) -> bool:

        if isinstance(mouse_pos, tuple): mouse_pos = Vector2().from_tuple(mouse_pos)

        img_size = Vector2(self.img.get_width(), self.img.get_height())
        real_pos = self.pos - img_size * self.pivot
        hor = mouse_pos.x > real_pos.x and mouse_pos.x < real_pos.x + img_size.x
        ver = mouse_pos.y > real_pos.y and mouse_pos.y < real_pos.y + img_size.y
        return hor and ver

def draw_many(window:pg.Surface, entities:list[Entity]):
    for ent in entities:
        ent.auto_draw(window)


def ents_to_sur(entities:list[Entity]) -> pg.Surface:

    subby_x = min(map(lambda x: x.pos.x - x.img.get_width() * x.pivot.x, entities))
    subby_y = min(map(lambda y: y.pos.y - y.img.get_height() * y.pivot.y, entities))

    sur_wid = max(map(lambda x: x.pos.x - x.img.get_width() * x.pivot.x - subby_x + x.img.get_width(), entities))
    sur_hei = max(map(lambda y: y.pos.y - y.img.get_height() * y.pivot.y - subby_y + y.img.get_height(), entities))

    sur = pg.Surface((sur_wid, sur_hei), pg.SRCALPHA)
    for ent in entities:
        
        dest_x = ent.pos.x - ent.img.get_width() * ent.pivot.x - subby_x
        dest_y = ent.pos.y - ent.img.get_height() * ent.pivot.y - subby_y
        dest = Vector2(dest_x, dest_y)

        sur.blit(ent.img, dest.to_tuple())
    
    return sur