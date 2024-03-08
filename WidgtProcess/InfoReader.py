import easyocr

from Resources.ImagesGrabedName import *
from ImageProcess import imageProcess

def get_capacity_result(reader):
    result = get_image_ocred(capacityImageName, reader)
    return result


def get_entity_selected_result(reader):
    img = imageProcess.get_full_screen()
    result = reader.readtext(img)
    result = get_image_ocred(entitySelectedImageName, reader)
    return result


def get_image_ocred(name, reader):

    # print("ocring: " + "ImagesGrabbed/" + name + ".png")

    result = reader.readtext("ImagesGrabbed/" + name + ".png")
    return result

if __name__ == "__main__":
    e = get_image_ocred("example")

    print(e)