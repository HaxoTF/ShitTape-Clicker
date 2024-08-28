import pygame as pg

def flat_colorize(img:pg.Surface, clr:pg.Color) -> pg.Surface:

    new_img = img.copy()
    for y in range(0, img.get_height()):
        for x in range(0, img.get_width()):
            c_clr = img.get_at((x, y))
            new_img.set_at((x, y), pg.Color(clr.r, clr.g, clr.b, c_clr.a))
    return new_img