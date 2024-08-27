import os
import pygame as pg
from vector import *
from entity import *

class FontMan:
    def __init__(self):
        self.images :list[pg.Surface] = []
        self.ident :list[str] = []
    
    def load(self, path:str) -> "FontMan":
        self.images = []
        self.ident = []

        for f in "0123456789abcdefghijklmnopqrstuvwxyz":
            img_path = os.path.join(path, f"{f}.png")
            
            if os.path.exists(img_path):
                self.images.append(pg.image.load(img_path))
                self.ident.append(f)

        return self
        
    def convert(self, text:int|str, base_pos:Vector2=Vector2(0, 0), base_pivot:Vector2=Vector2(0.5, 0.5)) -> list[Entity]:

        if isinstance(text, int): text = str(text)

        img_wid = self.images[0].get_width()
        img_hei = self.images[0].get_height()

        tot_wid = img_wid * (len(text)-1)

        ents :list[Entity] = []
        for i in range(0, len(text)):

            char = text[i]
            img_i = self.get_index(char)
            img = self.images[img_i]

            pos_x = (img_wid*i) - (tot_wid*base_pivot.x)

            ents.append(Entity(
                base_pos + Vector2(pos_x),
                0, img, base_pivot.copy()
            ))
        
        return ents

    def get_index(self, char:str) -> int:
        for i in range(0, len(self.ident)):
            if self.ident[i]==char: return i