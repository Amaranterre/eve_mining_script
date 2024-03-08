import pyautogui
import time

if __name__ == "__main__":
    while True:
        time.sleep(2)
        pos = pyautogui.position()
        print("[", pos.x,", ",pos.y,"]")
# [1736, 299] [116, 192] [1620, 107]