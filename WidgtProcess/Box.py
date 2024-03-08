def is_inside_box(pos1, pos2, box_position):
    top = box_position[0][1]
    bottom = box_position[1][1]
    left = box_position[0][0]
    right = box_position[1][0]

    if left <= pos1[0] <= right and left <= pos2[0] <= right and top <= pos1[1] <= bottom and top <= pos2[1] <= bottom:
        return True
    return False