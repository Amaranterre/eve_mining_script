from PIL import ImageGrab
import easyocr
import time
from EntityViewdList import EntityViewed

if __name__ == "__main__":
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext("ImagesGrabbed/test.png")

    print(result)