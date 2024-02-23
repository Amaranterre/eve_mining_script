from PIL import ImageGrab
import easyocr
import time
from EntityViewdList import entityViewed

reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext("ImagesGrabed/test.png")

print(result)