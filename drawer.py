import settings as s


class ClDrawer:
    def Draw(self, className, fields, compositions):
        pass


class HtmlClDrawer(ClDrawer):
    def __init__(self):
        self.__roundTable = '<<table border="1" style="rounded">'
        self.__endTable = '</table>>'


    def Draw(self, className, fields, compositions, aggregations):
        strDraw = self.__roundTable   
        strDraw += self.__DrawClassName (className)
        strDraw += self.__DrawFields (fields, compositions, aggregations)
        strDraw += self.__endTable
        return strDraw


    def __DrawClassName(self, name):
        return self.__AddCell(name, align="center", bgcolor="yellow", style="rounded", height=25)

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
        return self.__AddCell (name, upperbound=True, border=1) 

    def __AddEmptyCell(self, upperbound=False):
        if upperbound:
            return self.__AddCell ('', upperbound=True, height=10, border=1)
        return self.__AddCell ('', height=5)



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
        cell += f'>{name}</td></tr>'
        return cell
