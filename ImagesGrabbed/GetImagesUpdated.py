import time

from PIL import ImageGrab
from PIL import Image
import easyocr

from Resources.WidgetPosition import *
from Resources.ImagesGrabedName import *

fullScreenImageName = "fullScreen"


def getfullscreen():
    img = ImageGrab.grab()
    img.save(fullScreenImageName + ".png")


def get_capacity_image(img):
    box = (*capacityPositon[0], *capacityPositon[1])
    cropped = img.crop(box)
    cropped.save(capacityImageName + ".png")


def get_entity_selected_image(img):
    box = (*entitySelectedPosition[0], *entitySelectedPosition[1])
    cropped = img.crop(box)
    cropped.save(entitySelectedImageName + ".png")


def get_entity_view_list_image(img):
    box = (*entityViewListPosition[0], *entityViewListPosition[1])
    cropped = img.crop(box)
    cropped.save(entityViewListImageName + ".png")


def update():
    getfullscreen()
    img = Image.open(fullScreenImageName + ".png")

    get_capacity_image(img)
    get_entity_selected_image(img)
    get_entity_view_list_image(img)


if __name__ == "__main__":
    time.sleep(1)
    update()
