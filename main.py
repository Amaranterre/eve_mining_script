from PIL import ImageGrab
import easyocr
import time
from EntityViewdList  import entityViewdList


    


if __name__ == '__main__':
    list = entityViewdList()


    list.Update()
    
    
    
    list.Show()