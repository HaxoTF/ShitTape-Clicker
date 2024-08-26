import os
import pygame as pg
from vector import *

class NumMan:
    def __init__(self):
        self.images :list[pg.Surface] = []
    
    def load(self, path:str) -> "NumMan":
        self.images = []
        for i in range(0, 10):
            img_path = os.path.join(path, f"{i}.png")
            if not os.path.exists(img_path): raise FileExistsError(f"Couldn't find image: {img_path}")
            self.images.append(pg.image.load(img_path))
        return self

    def render(self, number:int=0) -> pg.Surface:

        img_wid = self.images[0].get_width()
        img_hei = self.images[0].get_height()
        str_num = str(number)
        
        sur = pg.Surface((img_wid*len(str_num), img_hei), pg.SRCALPHA)
        for i in range(0, len(str_num)):

            char = str_num[i]
            img  = self.images[int(char)]
            pos_x = img_wid*i

            sur.blit(img, (pos_x, 0))
        
        return sur