def wallpaper(lenght_room,width_room,height_room,width_wall,lenght_rollon):
    """
    >>> wallpaper(6.5,5.4,2.3,1.2,10,)
    5
    """
    import math
    result = math.ceil((math.ceil(((lenght_room + width_room) * 2) / width_wall)) / (math.floor(lenght_rollon / (height_room + 0.1))))
    return result