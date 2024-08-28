import pygame as pg
from upgrades import *
from fontman import *
from entity import *
from typing import Dict

imgs :Dict[str, pg.Surface] = {
    "ToiletPaper" : pg.image.load("images/toilet_paper.png"),
    "ToiletLeaf"  : pg.image.load("images/toilet_leaf.png"),
    "UpPlate"     : pg.image.load("images/up_plate.png"),
    "RichUpPlate" : pg.image.load("images/rich_up_plate.png"),
    "Shine"       : pg.image.load("images/shine.png")
}

fontmans :Dict[str, FontMan] = {
    "MBlack" : FontMan().load("images/wnums")
}

ups :Dict[str, Upgrade] = {
    "click"  : Upgrade("paper per click", 50, "linear"),
    "second" : Upgrade("paper per second", 50, "linear")
}

ups_ents :Dict[str, Entity] = {
    "click"   : Entity(Vector2(1020, 120).copy(), 0, imgs["UpPlate"]),
    "second"  : Entity(Vector2(1020, 340).copy(), 0, imgs["UpPlate"])
}