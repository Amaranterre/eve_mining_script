import random

def get_random_position(pos1, pos2):
    disX = abs(pos1[0] - pos2[0])
    disY = abs(pos1[1] - pos2[1])

    x = min(pos1[0], pos2[0])
    y = min(pos1[1], pos2[1])

    xx = int(x + disX * 0.5)
    yy = int(y + disY * 0.5)

    xx += random.randint(-3, 3)
    yy += random.randint(-3, 3)

    return (xx, yy)