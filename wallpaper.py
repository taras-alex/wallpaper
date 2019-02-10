def walleper(lenght_room,wight_room,height_room,wight_wall,lenght_rollon):
    """
    >>> walleper(6.5,5.4,2.3,1.2,10,)
    5
    """
    import math
    result = math.ceil((math.ceil(((lenght_room + wight_room) * 2) / wight_wall)) / (math.floor(lenght_rollon / (height_room + 0.1))))
    return result