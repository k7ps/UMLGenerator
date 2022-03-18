from PIL import ImageColor, ImageFont

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetDistTo(self, p2):
        return ( (self.x-p2.x)**2 + (self.y-p2.y)**2 )**0.5

class Set:
    rad = 20
    minlen = 200
    nameFont = ImageFont.truetype("helvetica.ttf", size=20)
    fieldFont = ImageFont.truetype("helvetica.ttf", size=13)
     
