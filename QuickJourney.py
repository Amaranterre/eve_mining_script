import pyautogui
import time
import random
import keyboard

from Resources.WidgetPosition import jumpButtonPositon



def get_random_position(pos1, pos2) :
    disX = abs(pos1[0] - pos2[0])
    disY = abs(pos1[1] - pos2[1])
    
    x = min(pos1[0], pos2[0])
    y = min(pos1[1], pos2[1])
    
    r = random.random()
    
    return (x + disX * r, y + disY * r)


def click(x, y):
    rTime = random.random() / 2
    pyautogui.moveTo(x, y, rTime)
    pyautogui.click()


def clickRandomly(pos1, pos2):
    rTime = random.random()
    time.sleep(rTime)
    
    rPos = get_random_position(pos1, pos2)
    click(*rPos)


def clickJumpRandomly():
    pos1 = jumpButtonPositon[0]
    pos2 = jumpButtonPositon[1]

    clickRandomly(pos1, pos2)



def setStopFlag():
    global stopflag
    stopflag = not stopflag

    if stopflag:
        print("关闭")
    else:
        print("开启")
def QuickJourney():
    global stopflag
    
    stopflag = False
    # set hot key

    
    while stopflag == False:
        # print("clicked")
        print("blStop: ",stopflag)
        clickJumpRandomly()

        time.sleep(2)
if __name__ == "__main__":
    time.sleep(5)

    keyboard.add_hotkey('ctrl+u',setStopFlag)

    global stopflag
    stopflag = True

    while True:
        if not stopflag:
            QuickJourney()
        time.sleep(2)
    
    # blStop = False
    # keyboard.add_hotkey('ctrl+z',setStopFlag)
    
    # while blStop == False:
    #     time.sleep(0.5)
    #     print("no")