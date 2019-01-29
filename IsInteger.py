def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False

is_int(7.0)   # True    
is_int(7.5)   # False    
is_int(-1)    # True    
