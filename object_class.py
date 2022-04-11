import settings as s

class ObjectClass:
    def __init__(self, name, variables, methods, parents, compositions):
        self.__name = name
        self.__vars = variables
        self.__methods = methods
        self.__parents = parents
        self.__compositions = compositions

    def Print(self):
        print('>', self.__name)
        print('\tVariables:',*self.__vars, sep='  ')
        print('\tMethods:', *self.__methods, sep='  ')
        print('\tParents:', *self.__parents, sep='  ')
        print('\tCompositions:', *self.__compositions, sep='  ')

    def Draw(self, draw, font, field_font, pos):
        rad = s.Set.rad
        minlen = s.Set.minlen 

        namesize = s.Point(*font.getsize(self.__name))
        size = s.Point(max(minlen, namesize.x+2*rad), namesize.y*(len(self.__vars)+len(self.__methods)+2))

        draw.rectangle((pos.x, pos.y, pos.x+size.x, pos.y+size.y), fill="black")
        draw.text((pos.x+(size.x-namesize.x)/2, pos.y+2), self.__name, fill='white', font=font)
        
        stPos = s.Point(pos.x+10, pos.y+namesize.y+3)
        for var in self.__vars:
            draw.text((stPos.x, stPos.y), var, fill='lightgrey', font=field_font)
            stPos.y += namesize.y+2
        for meth in self.__methods:
            draw.text((stPos.x, stPos.y), meth, fill='grey', font=field_font)
            stPos.y += namesize.y+2

    def GetImageSize(self, nameFont, fieldFont):
        rad = s.Set.rad
        minlen = s.Set.minlen 

        namesize = s.Point(*nameFont.getsize(self.__name))
        size = s.Point(max(minlen, namesize.x+2*rad), namesize.y*(len(self.__vars)+len(self.__methods)+2))
        
        return size

#a = ObjectClass('asf', ['a', 'b'], ['get', 'draw'], ['B'], [])
#a.Print()
