import time

from PIL import ImageGrab
from PIL import Image
import os

from Resources.WidgetPosition import *
from Resources.ImagesGrabedName import *

save_folder = "ImagesGrabbed"


def getfullscreen():
    img = ImageGrab.grab()

    save_path = os.path.join(save_folder, fullScreenImageName + ".png")
    img.save(save_path)


def crop_image(img, position, saving_name):
    box = (*position[0], *position[1])
    cropped = img.crop(box)

    save_path = os.path.join(save_folder, saving_name + ".png")
    cropped.save(save_path)


def get_capacity_image(img):
    crop_image(img, capacityPositon, capacityImageName)


def get_entity_selected_image(img):
    crop_image(img, entitySelectedPosition, entitySelectedImageName)


def get_entity_view_list_image(img):
    crop_image(img, entityViewListPosition, entityViewListImageName)


def get_out_station_buttom_image(img):
    crop_image(img, leaveStationPosition, leavingStationImageName)


def update_images():
    getfullscreen()

    path = os.path.join(save_folder, fullScreenImageName + ".png")
    img = Image.open(path)

    get_capacity_image(img)
    get_entity_selected_image(img)
    get_entity_view_list_image(img)
    get_out_station_buttom_image(img)


if __name__ == "__main__":
    # time.sleep(1)
    # update_images()

    time.sleep(1)
    getfullscreen()