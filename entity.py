import pygame as pg
from vector import *
from random import randint



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



class RigidEntity(Entity):
    def __init__(self, pos:Vector2=Vector2(0, 0), angle=0, img:pg.Surface=None, pivot:Vector2=Vector2(0.5, 0.5), base_vel:Vector2=Vector2(0, 0), vel_speed:float=1, gravity:float=1):
        super().__init__(pos, angle, img, pivot)
        self.vel       :Vector2 = base_vel
        self.vel_speed :float   = vel_speed
        self.gravity   :float   = gravity
    
    def process(self, delta_time:float):

        self.vel.move_towards(Vector2(0, 0), self.vel_speed*delta_time)
        self.vel.y += self.gravity*delta_time
        self.pos += self.vel
    
    def should_destroy(self, win_size:Vector2):
        return self.pos.y - self.img.get_height() > win_size.y



class Particles:
    def __init__(self, base_pos:Vector2=Vector2(0, 0), base_angle:float=0, img:pg.Surface=None, base_pivot:Vector2=Vector2(0.5, 0.5), vel_speed:float=1, vel_power:float=1, gravity:float=1) -> None:
        self.rents :list[RigidEntity] = []
        self.base_pos   :Vector2    = base_pos
        self.base_angle :Vector2    = base_angle
        self.img        :pg.Surface = img
        self.base_pivot :Vector2    = base_pivot
        self.vel_speed  :float      = vel_speed
        self.vel_power  :float      = vel_power
        self.gravity    :float      = gravity
    
    def add_parts(self, count:int=1):
        for i in range(0, count):
            vel_angle = randint(0, 360)
            velocity = Vector2().from_angle(vel_angle) * self.vel_power
            self.rents.append(RigidEntity(
                self.base_pos.copy(),
                self.base_angle,
                self.img,
                self.base_pivot,
                velocity,
                self.vel_speed,
                self.gravity
            ))
    
    def process_all(self, delta_time:float, win_size:Vector2) -> None:
        for re in self.rents:
            re.process(delta_time)
            if re.should_destroy(win_size):
                self.rents.remove(re)
    
    def draw_all(self, window:pg.Surface) -> None:
        for re in self.rents:
            re.auto_draw(window)


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