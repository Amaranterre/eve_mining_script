import easyocr

from Resources.ImagesGrabedName import *


def get_capacity_result():
    result = get_image_ocred(capacityImageName)
    return result


def get_entity_selected_result():
    result = get_image_ocred(entitySelectedImageName)
    return result


def get_image_ocred(name):
    reader = easyocr.Reader(['ch_sim', 'en'])

    print("ocring: " + "ImagesGrabbed/" + name + ".png")

    result = reader.readtext("ImagesGrabbed/" + name + ".png")
    return result


if __name__ == "__main__":
    e = get_image_ocred("example")

    print(e)