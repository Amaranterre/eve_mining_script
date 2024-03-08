import cv2
import numpy
import numpy as np
from cv2 import cvtColor
from PIL import ImageGrab
from PIL import Image

ratioMatched = 0.1 # 决定哪一个比率时，图片匹配
ScalingNumber = 10 # 放大图片；button的图片太小需要放大，而放大会影响descriptor

def image2numpy(img):
    np_img = np.array(img)
    return np_img


def np_image2gray(img):
    return cvtColor(img, cv2.COLOR_RGB2GRAY)


def image2gray(img):
    img = np.array(img)
    img = np_image2gray(img)
    return img

def get_full_screen():
    img = ImageGrab.grab()
    np_img = image2numpy(img)
    gray_img = np_image2gray(np_img)

    return gray_img


def cropped_screen_gn(pos1, pos2, scale=1):
    width = abs(pos1[0] - pos2[0])
    height = abs(pos1[1] - pos2[1])

    img = ImageGrab.grab(bbox=(*pos1, *pos2))

    if scale != 1:
        img = scalingimage(img, scale)
    # img.show()

    np_img = image2numpy(img)
    gray_img = np_image2gray(np_img)

    return gray_img


def screen_ocr(pos1, pos2, reader, is_full_screen = False):
    if is_full_screen:
        img = get_full_screen()
    else:
        img = cropped_screen_gn(pos1, pos2)
    return reader.readtext(img)


def crop_npimage(img, pos1, pos2):
    # print(pos1, "+", pos2)
    return img[pos1[1]:pos2[1], pos1[0]:pos2[0], ...]



def show_img(img):
    img.show()


def show_npimg(np_img):
    np_img = Image.fromarray(np_img)
    np_img.show()


def openwithscale(name):
    img = Image.open(name)
    if img is None:
        print("打不开 ", name)
    img = scalingimage(img, ScalingNumber)
    img = image2numpy(img)
    img = np_image2gray(img)
    return img




def save_numpy(np, s):
    img = Image.fromarray(np)
    img.save(s)


def reading_img(img, reader):
    return reader.readtext(img)

def read_screen(reader):
    img = ImageGrab.grab()
    img = image2gray(img)
    return reading_img(img, reader)


def crop_screen_nogray(pos1, pos2):
    img = ImageGrab.grab()
    img = numpy.array(img)
    img = crop_npimage(img, pos1, pos2)
    return img


def average_gray(np):
    size = np.size
    result = 0
    for row in np:
        sum = 0
        for el in row:
            if 70 <= el <= 90:
                print(el)
            sum += el
        #防溢出
        result += sum/size

    return result


def scalingimage(img, scale):

    width, height = img.size
    new_width = width * scale
    new_height = height * scale

    enlarged_image = img.resize((new_width, new_height), Image.BICUBIC)

    return enlarged_image


def get_kp(img, detector):
    kp, des = detector.detectAndCompute(img, None)

    # print(len(kp), des.shape)

    return kp

def howmatch(matches):
    sum = 0
    i = 0
    for match in matches:
        i += 1
        sum += match.distance
    return sum/i
def compare(img1, img2, detector):
    keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
    keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

    if (descriptors1 is None ) or (descriptors2 is None):
        print("no descriptor")
        return False

    # 创建Brute-Force匹配器
    bf = cv2.BFMatcher()

    # 使用KNN匹配器进行特征匹配
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append([m])

    return len(good_matches)

    # 绘制匹配结果
    # match_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None,
    #                             flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    #
    # show_npimg(match_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def collect_red_pixel(img):
    blue_channel = img[:, :, 2]
    green_channel = img[:, :, 1]
    red_channel = img[:, :, 0]

    # 创建一个布尔掩码，标识红色像素
    blue_less = blue_channel < 10
    green_less = green_channel < 10
    red_more = red_channel > 200
    red_mask = red_more & blue_less & green_less

    # print(img[100][99])
    # 统计红色像素数量
    red_pixel_count = np.sum(red_mask)
    return red_pixel_count

if __name__ == "__main__":
    ToolUsingPosition = [[1242, 175], [1312, 205]]
    img = cropped_screen_gn(*ToolUsingPosition)
    img = Image.fromarray(img)

    # sift = cv2.SIFT_create()
    #
    # img = Image.open("lockingButton_on.png")
    # img = scalingimage(img, ScalingNumber)
    # img = image2numpy(img)
    #
    # img1 = Image.open("lockingButton_able.png")
    # img1 = scalingimage(img1, ScalingNumber)
    # img1 = image2numpy(img1)
    #
    #
    # compare(img, img1, sift)

