from PIL import Image, ImageDraw, ImageColor, ImageFont

import settings as s
import object_class as o

class UI:
    def __init__(self):
        self.__size = s.Point(500, 500)
        self.__img = Image.new("RGB", (self.__size.x, self.__size.y), color='white')
        self.__draw = ImageDraw.Draw(self.__img)
        self.__classes = []

    def SetClasses(self, classes):
        self.__classes = classes

    def DrawUML(self):
        startPos = s.Point(10,10)
        pos = s.Point(startPos.x, startPos.y)
        maxHeight = 0
        for cl in self.__classes:
            sz = cl.GetImageSize(s.Set.nameFont, s.Set.fieldFont) 
            if pos.x + sz.x > self.__size.x:
                pos.x = startPos.x
                pos.y += maxHeight+4
                maxLastY = sz.y
            cl.Draw(self.__draw, s.Set.nameFont, s.Set.fieldFont, pos)
            maxHeight = max(maxHeight, sz.y)
            pos.x += sz.x + 5

        self.__img.save("ex.png", "PNG")
