import random

import keyboard
import time
import pyautogui
from enum import Enum
import logging

from QuickJourney import clickRandomly
from EntitySelected import get_entity_selected
from QuickJourney import get_random_position
from ImageProcess.imageProcess import *
from InfoReader import *


from Resources.WidgetPosition import *

MineralList = ["凡晶石", "富凡晶石", "厚质凡晶石", "灼烧岩", "厚灼烧岩", "浓缩灼烧岩"]
WantedMineralList = ["凡晶石", "富凡晶石", "厚质凡晶石"]
miningKeyword = "凡晶"

StoringStation = "皮尔米特2-"
MiningSite = "皮尔米特10"
toolDistanceMax = 9500
RedPixel_On = 2000

def log(s):
    global logger
    logger.info(s)



class ShipPosition(Enum):
    InStation = 1
    OutStation = 2


def get_ship_position():
    global reader

    img = crop_screen(*leaveStationPosition)
    result = reader.readtext(img)

    def selector(feature):
        # print(feature[1])
        if feature[1] == "离站":
            return True
        return False

    feature = iter_result(result, selector)
    if feature is None:
        return ShipPosition.OutStation
    return ShipPosition.InStation




def is_inside_box(pos1, pos2, box_position):
    top = box_position[0][1]
    bottom = box_position[1][1]
    left = box_position[0][0]
    right = box_position[1][0]

    if left <= pos1[0] <= right and left <= pos2[0] <= right and top <= pos1[1] <= bottom and top <= pos2[1] <= bottom:
        return True
    return False


def space_del(s):
    s = s.replace(" ","")
    return s


def ismineral(content):
    for mineral in WantedMineralList:
        if space_del(content) == mineral:
            return True
    return False


def iter_result(result, selector):
    for feature in result:
        if selector(feature):
            return feature


def click_feature(result, selector):
    for feature in result:
        if selector(feature):
            clickRandomly(pos1=feature[0][0], pos2=feature[0][2])
            return True
    return False


def go_back_station():
    global reader
    time.sleep(1)
    log("开始返回空间站")
    if get_ship_position() == ShipPosition.InStation:
        log("已经返回空间站")
        return True
    #切换到空间站表
    clickRandomly(*stationListerPosition)
    result = read_screen(reader)
    # 点击要回去的空间站
    def selector(feature):
        if is_inside_box(feature[0][0], feature[0][2], entityViewListPosition) and (space_del(feature[1]) == StoringStation):
            return True
        return False

    feature = iter_result(result, selector)
    if feature is None:
        log("找不到要回去的空间站")
        return False
    clickRandomly(feature[0][0],feature[0][2])


    log("开始“停靠”")

    cnt = 0
    while (get_ship_position() == ShipPosition.OutStation) and (cnt <= 30):
        cnt += 1
        clickRandomly(*stationingButtonPosition)
        time.sleep(1)

    if get_ship_position() == ShipPosition.InStation:
        log("已经返回空间站")
        return True
    else:
        log("返回时间过长，重新开始返回")
        return False

def go_out_station():
    time.sleep(1)
    if get_ship_position() == ShipPosition.OutStation:
        return True
    clickRandomly(*leaveStationPosition)


def fetch_mineral():
    global reader
    time.sleep(1)
    def selector(feature):
        # print(feature[1])
        if is_inside_box(feature[0][0], feature[0][2], entityViewListPosition) and ismineral(feature[1]):
            return True
        return False



    entity = get_entity_selected(reader)
    if entity is None:
        log("没有选择矿石")
    else:
        log("矿石选择成功")
        return True


    clickRandomly(*mineralListerPosition)
    result = read_screen(reader)
    feature = iter_result(result, selector)
    if feature is None:
        log("找不到矿石")
        return False
    clickRandomly(feature[0][0], feature[0][2])


def get_closed():
    time.sleep(1)
    clickRandomly(*encircleButtonPosition)
    time.sleep(1)

    global reader
    entity = get_entity_selected(reader)

    if entity.distance < 50:
        return False
    if entity.distance < toolDistanceMax - 3000:
        return True


def is_locked():
    cur_img = crop_screen_nogray(*lockingButtonPosition)
    cur_img = Image.fromarray(cur_img)
    cur_img = scalingimage(cur_img, ScalingNumber)

    cur_img = numpy.array(cur_img)
    if collect_red_pixel(cur_img) > RedPixel_On:
        return True
    return False

def locking():
    pyautogui.moveTo(1059 ,  250)
    time.sleep(0.3)
    if is_locked():
        return True
    clickRandomly(*lockingButtonPosition)
    time.sleep(5)


def myscale(img):
    img = Image.fromarray(img)
    img = scalingimage(img, 10)
    img = numpy.array(img)
    return img


def start_mining():
    pos1 = OneToolPosition[0]
    pos2 = OneToolPosition[1]
    clickRandomly(pos1,pos2)

    #图像识别太难了。。。
    for i in range(2):
        pos1[0] += 5
        pos2[0] += 5
        clickRandomly(pos1,pos2)
        pos1[0] += 10
        pos2[0] += 10
        clickRandomly(pos1, pos2)
        pos1[0] -= 15
        pos2[0] -= 15
        clickRandomly(pos1, pos2)
        pos1[0] -= 15
        pos2[0] -= 15
        clickRandomly(pos1, pos2)
        pos1[0] += 15
        pos2[0] += 15
        pos1[1] += 15
        pos2[1] += 15
    pos1[1] -= 30
    pos2[1] -= 30
    lauch_tool()

    return True

def is_full_loaded(reader):
    time.sleep(1)
    img = crop_screen(*capacityPositon)
    # Image.fromarray(img).show()
    result = reader.readtext(img)
    # print(result)
    if result is None:
        log("找不到货舱容量")
        return True
    content = result[0][1]
    raw_number = ""

    for ch in content:
        if ch == "/":
            break
        if ch.isdigit():
            raw_number += ch

    # log("当前货舱体积:" + raw_number)
    global capacity
    capacity = raw_number
    if raw_number == "50000":
        return True
    return False


def lauch_tool():
    keyboard.press_and_release("F1")
    time.sleep(0.2)
    keyboard.press_and_release("F2")
    time.sleep(0.2)
    keyboard.press_and_release("F")




def unload():
    def press_ctrl_a():
        keyboard.press("ctrl")
        keyboard.press("a")
        time.sleep(0.1)  # 等待一段时间，确保按键生效
        keyboard.release("a")
        keyboard.release("ctrl")
    def drag(posfrom, posto):
        pyautogui.moveTo(*posfrom, duration=random.random())
        pyautogui.mouseDown()
        pyautogui.moveTo(*posto, duration=random.random())
        pyautogui.mouseUp()

    pos = itemInShipPositions[0]
    point_from = get_random_position(pos[0], pos[1])
    point_to = get_random_position(itemStoragePostion[0], itemStoragePostion[1])

    pyautogui.moveTo(*point_from, duration=random.random())
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    press_ctrl_a()
    time.sleep(0.5)
    drag(point_from, point_to)

def go_back_mining_site():
    time.sleep(1)
    global reader

    clickRandomly(*miningSiteListerPosition)
    result = read_screen(reader)

    # 点击要回去的空间站
    def selector(feature):
        if is_inside_box(feature[0][0], feature[0][2], entityViewListPosition) and (
                space_del(feature[1]) == MiningSite):
            return True
        return False

    feature = iter_result(result, selector)
    if feature is None:
        log("找不到要去矿带")
        return False




    clickRandomly(feature[0][0], feature[0][2])


    time.sleep(1)
    clickRandomly(*reachingButtonPosition)
    time.sleep(35)

    entity = get_entity_selected(reader)
    if entity is None:
        return False
    # print(entity.distance)

    if entity.distance == -1:
        return False
    return True


def init():
    global reader
    global SIFT
    reader = easyocr.Reader(['ch_sim', 'en'])
    SIFT = cv2.SIFT_create()

    get_logger()


def debug_automining():
    init()
    global reader
    time.sleep(1)
    log("开始debug")

    while True:
        if get_ship_position() == ShipPosition.InStation:
            unload()
            log("卸货")
            while not go_out_station():
                pass
            log("出站")
            while not go_back_mining_site():
                pass
            log("到达矿场")


        if get_ship_position() == ShipPosition.OutStation:
            is_full = False
            while True:
                while not fetch_mineral():
                    pass
                log("找到一块矿石")
                while not get_closed():
                    pass
                while not get_closed():
                    pass
                log("已经接近矿石")
                while not locking():
                    pass
                time.sleep(10)
                while not start_mining():
                    pass
                log("开始锁定并挖矿")

                global capacity
                lastcapacity = 0
                cnt = 0

                while True:
                    time.sleep(10)
                    #采矿机器人
                    keyboard.press_and_release('f')
                    if cnt >= 10:
                        log("货舱长时间不变，重启")
                        break

                    if is_full_loaded(reader):
                        is_full = True
                        log("货舱已满，回家")
                        break
                    if get_entity_selected(reader) is None:
                        log("矿石挖完了")
                        break
                    if lastcapacity == capacity:
                        cnt += 1
                    else:
                        lastcapacity = capacity
                if is_full:
                    break
            while not go_back_station():
                pass


def get_logger():
    global logger
    # 配置日志记录器
    logging.basicConfig(level=logging.DEBUG,  # 设置日志级别为DEBUG
                        format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
                        filename='app.log',  # 将日志写入文件
                        filemode='w')  # 写入模式为覆盖模式
    # 创建日志记录器
    logger = logging.getLogger()

    global reader
    reader = easyocr.Reader(['ch_sim','en'])




if __name__ == "__main__":
    init()

    # while True:
    #     while not locking():
    #         pass
    #     while not start_mining():
    #         pass

    debug_automining()

