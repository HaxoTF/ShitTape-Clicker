import os
import pygame as pg
from vector import *
from entity import *

normal_index = "0123456789abcdefghijklmnopqrstuvwxyz"
special_index = [
    [".", "dot"],
    ["!", "exclamation"],
    ["?", "question"],
    ["$", "dollar"],
    ["#", "hash"],

    # Math
    ["-",  "minus"],
    ["+",  "plus"]
]

class FontMan:
    def __init__(self):
        self.images :list[pg.Surface] = []
        self.ident :list[str] = []
    
    def load(self, path:str) -> "FontMan":
        self.images = []
        self.ident = []

        # digits and letters
        for f in normal_index:
            img_path = os.path.join(path, f"{f}.png")
            
            if os.path.exists(img_path):
                self.images.append(pg.image.load(img_path))
                self.ident.append(f)
        
        # special
        special_path = os.path.join(path, "special")
        if os.path.exists(special_path):
            for f in special_index:
                img_path = os.path.join(special_path, f"{f[1]}.png")

                if os.path.exists(img_path):
                    self.images.append(pg.image.load(img_path))
                    self.ident.append(f[0])

        return self
        
    def convert(self, text:int|str, base_pos:Vector2=Vector2(0, 0), base_pivot:Vector2=Vector2(0.5, 0.5), font_size:float=1) -> list[Entity]:

        if isinstance(text, int): text = str(text)

        img_wid = self.images[0].get_width() * font_size
        img_hei = self.images[0].get_height() * font_size
        tot_wid = img_wid * (len(text)-1)

        ents :list[Entity] = []
        for i in range(0, len(text)):

            char = text[i]
            img_i = self.get_index(char)
            if img_i == None: continue
            img = self.images[img_i]

            if font_size!=1:
                new_size = Vector2(img.get_width(), img.get_height()) * font_size
                img = pg.transform.scale(self.images[img_i], new_size.to_tuple())
            else: 
                img = self.images[img_i]

            pos_x = (img_wid*i) - (tot_wid*base_pivot.x)

            ents.append(Entity(
                base_pos + Vector2(pos_x),
                0, img, base_pivot.copy()
            ))
        
        return ents

    def to_sur(self, text:int, font_size:float=1) -> pg.Surface:
        ents = self.convert(text, Vector2(0, 0), Vector2(0.5, 0.5), font_size)
        return ents_to_sur(ents)

    def get_index(self, char:str) -> int:

        for i in range(0, len(self.ident)):
            if self.ident[i]==char: return i