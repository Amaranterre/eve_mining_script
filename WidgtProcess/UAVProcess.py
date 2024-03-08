import time

from ImageProcess.imageProcess import screen_ocr
from Resources.WidgetPosition import UAVBox
from Iterator.iterator import iter_resultset
from Clicker.my_keyboard import key_enter

import easyocr


UAVnameset = ["采矿无人机"]
totalUAVnum = 2

def get_inside_UAV(reader):
    result = screen_ocr(*UAVBox, reader)
    def selector(feature):
        for name in UAVnameset:
            if name in feature[1]:
                return True
        return False
    def breaking(feature):
        if "太空" in feature[1]:
            return True

    set = iter_resultset(result,selector, breaker=breaking)
    return set

def get_outside_UAV(reader):
    result = screen_ocr(*UAVBox, reader)
    def selector(feature):
        for name in UAVnameset:
            if name in feature[1]:
                return True
        return False

    def closure(flag):
        def unti(feature):
            nonlocal flag
            if flag or ("太空" in feature[1]):
                # print("Ding!")
                flag = True
                return True
            else:
                return False
        return unti


    set = iter_resultset(result, selector, until=closure(False) )
    return set


def releaseUAV(reader):
    for i in range(5):
        outUAV = get_outside_UAV(reader)
        if len(outUAV) == totalUAVnum:
            return True

        key_enter("shift","f")
        time.sleep(2)

    raise ValueError("can't release UAV")


def collectUAV(reader):
    for i in range(5):
        inUAV = get_inside_UAV(reader)
        if len(inUAV) == totalUAVnum:
            return True

        key_enter("shift","r")
        time.sleep(10)

    print("can't collect UAV")
    raise False


if __name__ == "__main__":
    reader = easyocr.Reader(['ch_sim', 'en'])



        # print("inside", set1)
        # print("outside", set2)
    try:
        collectUAV(reader)
    except ValueError as e:
        print("error", e)

    time.sleep(2)