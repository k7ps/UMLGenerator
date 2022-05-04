from settings import *


#@UML clusters Drawing
class ClDrawer:
    def Draw(self, className, fields, compositions):
        pass


#@UML clusters Drawing
class HtmlClDrawer(ClDrawer):
    def __init__(self):
        self.__roundTable = f'<<table border="{Set.clBorder}" style="{Set.clStyle}">'
        self.__endTable = '</table>>'


    def Draw(self, className, fields, compositions, aggregations):
        strDraw = self.__roundTable   
        strDraw += self.__DrawClassName (className)
        strDraw += self.__DrawFields (fields, compositions, aggregations)
        strDraw += self.__endTable
        return strDraw


    def __DrawClassName(self, name):
        return self.__AddCell(name, align="center", bgcolor=Set.nameCol, style="rounded", height=Set.nameHeight)

    def __IsMethod(self, method):
        return len(method)>2 and method[-2:] == '()'

    def __DrawFields(self, fields, compositions, aggregations):
        strVars = ''
        strMethods = ''

        for field in fields:
            if self.__IsMethod(field):
                strMethods += self.__DrawMethod(field, len(strMethods)==0)
            else:
                strVars += self.__DrawVar(field, compositions, aggregations)

        if not strVars:
            strVars += self.__AddEmptyCell()
        if not strMethods:
            strMethods += self.__AddEmptyCell (upperbound=True)

        return strVars + strMethods

    def __DrawVar(self, var, compositions, aggregations):
        if compositions.get(var) != None or aggregations.get(var) != None:
            return self.__AddPortCell (var)
        return self.__AddCell (var)

    def __DrawMethod(self, method, empty):
        if empty:
            return self.__AddUpperBoundCell (method)
        return self.__AddCell (method)


    def __AddPortCell(self, name):
        return self.__AddCell (name, port=name)

    def __AddUpperBoundCell(self, name):
        return self.__AddCell (name, upperbound=True, border=Set.splitThick) 

    def __AddEmptyCell(self, upperbound=False):
        if upperbound:
            return self.__AddCell ('', upperbound=True, height=Set.emptyBoundCellHeight, border=Set.splitThick)
        return self.__AddCell ('', height=Set.emptyCellHeight)



    def __AddCell(self, name, align="left", upperbound=False, border=0, bgcolor='transparent', 
                  width=None, height=None, port=None, style=None):
        cell = f'<tr><td border="{border}" align="{align}" bgcolor="{bgcolor}" '
        if style != None:
            cell += f'style="{style}" ' 
        if upperbound:
            cell += f'sides="t" '
        if width != None:
            cell += f'width="{width}"'
        if height != None:
            cell += f'height="{height}"'
        if port != None:
            cell += f'port="{port}" '

        if name != "":
            cell += f'><font point-size="{Set.clFontSize}">{name}</font></td></tr>'
        else:
            cell += f'></td></tr>'
        return cell
