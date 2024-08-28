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



def cut_round(value:float) -> float:
    if str(int(value))==str(value): return value
    else: return int(value)



def short_num(value:float) -> str:

    units = "kmb"

    if value >= 1000:
        i = -1
        for u in units:
            if value >= 1000:
                value /= 1000
                i += 1
            else: break
        return f"{round(value, 1)}{units[i]}"        
    
    return str(value)