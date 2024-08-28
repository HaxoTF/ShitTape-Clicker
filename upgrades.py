from typing import Literal
from entity import *
from fontman import *
import copy

class Upgrade:
    def __init__(self, name:str, base_cost:int, inf_meth=Literal["linear", "double", "tens"]):
        self.name = name
        self.base_cost :int = base_cost
        self.inf_meth :Literal["linear", "double", "tens"] = inf_meth
        self.cost = base_cost
        self.level = 1

    def can_buy(self, money:int) -> bool:
        return money >= self.cost
    
    def upgrade(self):
        self.level += 1

        match self.inf_meth:
            case "double": self.cost *= 2
            case "tens": self.cost *= 10
            case "linear": self.cost = self.level * self.base_cost