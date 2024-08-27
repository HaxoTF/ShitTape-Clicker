from upgrades import *
from fontman import *
from typing import Dict

ups :Dict[str, Upgrade] = {
    "click" : Upgrade(50, "double")
}

fontmans :Dict[str, FontMan] = {
    "MBlack" : FontMan().load("images/wnums")
}