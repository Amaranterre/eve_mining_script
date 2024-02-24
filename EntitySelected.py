import time

from ImageProcess.imageProcess import *
from EntityViewdList import EntityViewed
from InfoReader import get_entity_selected_result
from Resources.WidgetPosition import *

entityNoneWord = "没有选择物体"


###unit: meter
def alter_to_number(str_now):
    raw_number = ""
    str_now = str_now.replace(" ", "")

    print(raw_number)

    flag = True
    for ch in str_now:
        if ch == ",":
            continue
        if ch.isdigit():
            raw_number += ch
        if ch == "." and flag:
            raw_number += ch
            flag = False

    if len(raw_number) >= 1 and raw_number[-1] == ".":
        raw_number += "0"
    try:
        number = float(raw_number)
    except:
        print("cant convert", raw_number)
        return -1

    unit = str_now[-2:]
    if unit == "km":
        number *= 1000
    if unit == "AU":
        return -1

    return number


def get_entity_selected(reader):
    img = crop_screen(*entitySelectedPosition)
    result = reader.readtext(img)
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
