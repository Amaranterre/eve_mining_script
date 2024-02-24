from PIL import ImageGrab
import ImageProcess
from PIL import Image

SecondButtonPosition = [[1382, 173], [1420, 207]]
ThirdButtonPosition = [[1422, 173], [1454, 206]]
FourthButtonPosition = [[1454, 170], [1494, 210]]
FifthButtonPosition = [[ 1494 ,  180 ],[ 1526 ,  208 ]]
SixthButtonPosition = [[1527, 173], [1563, 209]]

ToolUsingPosition = [[ 1242 ,  175 ],[ 1312 ,  205 ]]

if __name__ == "__main__":
    img = ImageGrab.grab()
    img = ImageProcess.image2numpy(img)
    img = ImageProcess.np_image2gray(img)
    img = ImageProcess.crop_npimage(img, *ToolUsingPosition)

    img = Image.fromarray(img)
    img.save("toolView2_gray.png")
    img.show()

