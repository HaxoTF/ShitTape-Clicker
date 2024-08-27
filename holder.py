import pygame as pg
from upgrades import *
from fontman import *
from entity import *
from typing import Dict

imgs :Dict[str, pg.Surface] = {
    "ToiletPaper" : pg.image.load("images/toilet_paper.png"),
    "ToiletLeaf"  : pg.image.load("images/toilet_leaf.png"),
}

ups :Dict[str, Upgrade] = {
    "click" : Upgrade(50, "double")
}

fontmans :Dict[str, FontMan] = {
    "MBlack" : FontMan().load("images/wnums")
}