import keyboard
import random
import time
def key_enter(*keys):
    for key in keys:
        keyboard.press(key)
        time.sleep(random.random()/2)

    for key in keys:
        keyboard.release(key)


if __name__ == "__main__":
    time.sleep(1)
    key_enter("shift", "f")

