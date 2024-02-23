import time

from EntityViewdList import EntityViewed
from InfoReader import get_entity_selected_result

entityNoneWord = "没有选择物体"


###unit: meter
def alter_to_number(str_now):
    raw_number = ""
    for ch in str_now:
        if ch.isdigit() or ch == ".":
            raw_number += ch

    number = float(raw_number)

    unit = str_now[-2:]
    if unit == "km":
        number *= 1000

    print(number)

    return number


def get_entity_selected():
    result = get_entity_selected_result()

    entity = EntityViewed()

    try:
        name = result[0][1]
        str_entity_distance = result[1][1]
    except IndexError:
        print("entitySelected图像异常")
        return None

    if name == entityNoneWord:
        return None

    distance = alter_to_number(str_entity_distance)

    entity.distance = distance
    entity.name = name
    return entity


def show(entity):
    print("name: ", entity.name)
    print("distace: ", entity.distance)


if __name__ == "__main__":
    e = get_entity_selected()
    show(e)

    print("sleeping..")
    time.sleep(1)
    print("wake")

    e = get_entity_selected()
    show(e)
