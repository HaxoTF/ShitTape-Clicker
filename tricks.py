def move_towards(value:float, target:float, by:float) -> float:

    if value < target:
        value += by
        value = min(value, target)
        return value

    if value > target:
        value -= by
        value = max(value, target)
        return value
    
    return value