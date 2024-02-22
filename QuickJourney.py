import pyautogui
import time
import random
import keyboard

jumpButtonPositon = [[1425,180], [1448, 202]]

def getRandomPosition(pos1, pos2) :
    disX = abs(pos1[0] - pos2[0])
    disY = abs(pos1[1] - pos1[1])
    
    x = min(pos1[0], pos2[0])
    y = min(pos1[1], pos2[1])
    
    r = random.random()
    
    return (x + disX * r, y + disY * r)

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def clickJumpRandomly():
    rTime = random.random()
    time.sleep(rTime)
    
    pos1 = jumpButtonPositon[0]
    pos2 = jumpButtonPositon[1]

    rPos = getRandomPosition(pos1, pos2)

    click(*rPos)

def setStopFlag():
    global blStop
    blStop = True
    print("inFunction, blstop: ", blStop)

def QuickJourney():
    global blStop
    
    blStop = False
    # set hot key
    keyboard.add_hotkey('ctrl+u',setStopFlag)
    
    while blStop == False:
        time.sleep(2)
        # print("clicked")
        # print("blStop: ",blStop)
        clickJumpRandomly()

if __name__ == "__main__":
    time.sleep(5)
    QuickJourney()
    
    # blStop = False
    # keyboard.add_hotkey('ctrl+z',setStopFlag)
    
    # while blStop == False:
    #     time.sleep(0.5)
    #     print("no")