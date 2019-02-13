def wallpaper(lenght_room, width_room, height_room, width_wall, lenght_rollon):
    """
    >>> wallpaper(6.5,5.4,2.3,1.2,10,)
    5
    """
    import math
    k = 0.1  # запас длины рулона
    perimeter_room = (lenght_room + width_room) * 2
    rollon = math.floor(lenght_rollon / (height_room + k))
    result = math.ceil((math.ceil(perimeter_room / width_wall)) / rollon)
    return result
