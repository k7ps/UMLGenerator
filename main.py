from PIL import Image, ImageDraw, ImageColor, ImageFont

import obj
import settings as s

img = Image.new("RGB", (500, 500), color='white')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("helvetica.ttf", size=20)
font2 = ImageFont.truetype("helvetica.ttf", size=13)

a = obj.ObjectClass('Enemy',['health', 'damage', 'point', 'armor'],['Hit','Die','UpLevel'],[],[])
a.Draw(draw, font, font2, s.Point(50,10))

img.save("ex.png", "PNG")
