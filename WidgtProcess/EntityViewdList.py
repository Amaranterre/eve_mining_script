from WidgtProcess.InfoReader import get_image_ocred

entityViewListImageName = "entityViewListImage"

# widthDistance =
# widthName =
# widthTypeInner =
# widthSize =
# widthVelocity =
rangeWidth = [0, 110, 300, 410, 490, 570]
heightFeature = 25



def GetFeatureCenter(featureFrame):
    pos1 = featureFrame[0]
    pos2 = featureFrame[2]

    return [(pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2]


def GetCoodinate(center):
    row = center[1] / heightFeature

    posX = center[0]
    for i in range(5):
        if rangeWidth[i] <= posX <= rangeWidth[i + 1]:
            return [row, i]


class EntityViewed:
    def __init__(self, distance=None, name=None, type_viewed=None, size=None, velocity=None, pos1=None, pos2=None):
        self.distance = distance
        self.name = name
        self.typeInner = type_viewed
        self.size = size
        self.velocity = velocity
        self.pos1 = pos1
        self.pos2 = pos2

def get_view_list_data():
    return get_image_ocred(entityViewListImageName)


class entityViewdList:

    def Update(self):
        result = get_view_list_data()

        self.list = []

        rowNow = 0
        entityNow = EntityViewed(None, None, None, None, None)

        for feature in result:

            featureContent = feature[1]
            print(featureContent)
            featureFrame = feature[0]

            featureCenter = GetFeatureCenter(featureFrame)
            listCoodinate = GetCoodinate(featureCenter)

            if listCoodinate[1] == 0:
                entityNow.distance = featureContent
            if listCoodinate[1] == 1:
                entityNow.name = featureContent
            if listCoodinate[1] == 2:
                entityNow.typeInnner = featureContent
            if listCoodinate[1] == 3:
                entityNow.size = featureContent
            if listCoodinate[1] == 4:
                entityNow.velocity = featureContent

            if rowNow != listCoodinate[0]:
                rowNow = listCoodinate[0]
                self.list.append(entityNow)

        self.list.append(entityNow)

    def Show(self):
        i = 0
        for entity in self.list:
            print("ENTITY", i, ":")
            print("\t", "距离", entity.distance)
            print("\t", "名字", entity.name)
            print("\t", "类型", entity.typeInner)
            print("\t", "大小", entity.size)
            print("\t", "速度", entity.velocity)
            print("*******")
            i += 1
