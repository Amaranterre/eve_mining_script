from EntityViewdList import get_view_list_data
from QuickJourney import clickRandomly
from EntitySelected import get_entity_selected
import time

from Resources.WidgetPosition import encircleButtonPosition

from InfoReader import get_capacity_result

MineralList = ["凡晶石", "富凡晶石", "灼烧岩", "厚灼烧岩", "浓缩灼烧岩"]


stationName = "皮尔米特9-"

toolDistanceMax = 9500


def is_mining_ok():
    return


def ismineral(content):
    for mineral in MineralList:
        if content == mineral:
            return True
    return False


def fetch_mineral():
    isFetched = False
    
    result = get_view_list_data()
    
    for feature in result:
        content = feature[1]
        pos1 = feature[0][0]
        pos2 = feature[0][2]
        
        if ismineral(content):
            clickRandomly(pos1, pos2)
            return True
    return False


def click_encircle():
    pos1 = encircleButtonPosition[0]
    pos2 = encircleButtonPosition[1]
    
    clickRandomly(pos1, pos2)


def is_full_loaded():
    result = get_capacity_result()
    
    content = result[0][1]
    raw_number = ""
    
    for ch in content:
        if ch == "/":
            break
        if ch.isdigit():
            raw_number += ch
    
    if raw_number == "50000":
        return True
    return False


def mining():
    while is_mining_ok():
        entity = get_entity_selected()

        if entity == None:
            if not fetch_mineral():
                break
        
            time.sleeep(1)
            continue    
        if entity.distance > toolDistanceMax:
            click_encircle()
        if is_full_loaded():
            goToStation()
            #...........


if __name__ == "__main__":
    time.sleep(1)