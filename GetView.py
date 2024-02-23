from PIL import ImageGrab
import easyocr
import time

from EntityViewdList import entityViewListPosition
from EntityViewdList import entityViewListImageName

if __name__ == "__main__":
    reader = easyocr.Reader(['ch_sim','en'])
        
    img = ImageGrab.grab(bbox=(entityViewListPosition))
    img.save(entityViewListImageName + ".png")