import settings as s


class ClDrawer:
    def Draw(self, className, variables, methods, compositions):
        pass


class HtmlClDrawer(ClDrawer):
    def __init__(self):
        self.__roundTable = '<<table border="1" style="rounded">'
        self.__endTable = '</table>>'


    def Draw(self, className, variables, methods, compositions):
        strDraw = self.__roundTable   
        strDraw += self.__DrawClassName (className)
        strDraw += self.__DrawVars (variables, compositions)
        strDraw += self.__DrawMethods (methods)
        strDraw += self.__endTable
        return strDraw



    def __DrawClassName(self, name):
        return self.__AddCell(name, align="center", bgcolor="yellow", style="rounded", height=25)


    def __DrawVars(self, variables, compositions):
        if len(variables) == 0:
            return self.__AddEmptyCell()

        strVars = ''
        for var in variables:
            if compositions.get(var) == None:
                strVars += self.__AddCell (var)
            else:
                strVars += self.__AddPortCell (var)

        return strVars


    def __DrawMethods(self, methods):
        if len(methods) == 0:
            return self.__AddEmptyCell (upperbound=True)

        strMethods = ''
        strMethods += self.__AddUpperBoundCell (methods[0])
        for i in range(1, len(methods)):
            strMethods += self.__AddCell (methods[i])

        return strMethods



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
