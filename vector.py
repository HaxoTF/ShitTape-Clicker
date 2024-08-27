from tricks import *
import math

class Vector2:
    def __init__(self, x:float=0, y:float=0) -> None:
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("x and y must be of type float or int")
        
        self.x :float = x
        self.y :float = y
    
    # copy
    def copy(self) -> "Vector2":
        return Vector2(self.x, self.y)

    # TUPLE
    def from_tuple(self, a:tuple[float, float]) -> "Vector2":
        self.x = a[0]
        self.y = a[1]
        return self
    
    def to_tuple(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def move_towards(self, target:"Vector2", by:float) -> None:
        self.x = move_towards(self.x, target.x, by)
        self.y = move_towards(self.y, target.y, by)
    
    def to_angle(self) -> float:
        return math.degrees(math.atan2(self.y, self.x))

    def from_angle(self, angle:float) -> "Vector2":
        radians = math.radians(angle)
        self.x = math.cos(radians)
        self.y = math.sin(radians)
        return self

    # ------------------------------ SPECIAL METHODS -----------------------------------

    # String
    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    # Apply
    def _aop(self, other, op) -> "Vector2":
        if isinstance(other, Vector2):
            return Vector2(op(self.x, other.x), op(self.y, other.y))
        elif isinstance(other, (float, int)):
            return Vector2(op(self.x, other), op(self.y, other))
        elif isinstance(other, (tuple, list)):
            if len(other) != 2: raise ValueError("Tuple/List must be 2 in length")
            return Vector2(op(self.x, other[0]), op(self.y, other[1]))
    
    def __add__(self, other) -> "Vector2":
        return self._aop(other, lambda a,b: a+b) 
    def __sub__(self, other) -> "Vector2":
        return self._aop(other, lambda a,b: a-b)
    def __mul__(self, other) -> "Vector2":
        return self._aop(other, lambda a,b: a*b)
    def __truediv__(self, other) -> "Vector2":
        return self._aop(other, lambda a,b: a/b)