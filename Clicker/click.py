import pyautogui
import random
import time
from Clicker.pos import get_random_position


def click(x, y):
    rTime = random.random() / 2
    pyautogui.moveTo(x, y, rTime)
    pyautogui.click()


def clickRandomly(pos1, pos2):
    rTime = random.random()
    time.sleep(rTime)

    rPos = get_random_position(pos1, pos2)
    click(*rPos)


def click_feature(result, selector):
    for feature in result:
        if selector(feature):
            clickRandomly(pos1=feature[0][0], pos2=feature[0][2])
            return True
    return False