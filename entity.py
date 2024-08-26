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