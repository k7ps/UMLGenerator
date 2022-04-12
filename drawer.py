import settings as s

class ClDrawer:
    def Draw(self, name, vs, ms):
        pass

class HtmlClDrawer(ClDrawer):
    def __init__(self):
        pass

    def Draw(self, name, vs, ms):
        drow = '<<table border="1" style="rounded">'
        drow += self.__AddCell(name, bgcolor="yellow", style="rounded", height=25)

        for var in vs:
            drow += self.__AddCell(var, align='left')

        first = False
        if len(ms) == 0:
            drow += self.__AddCell('', bound=True, height=8, border=1)
        for meth in ms:
            if not first:
                drow += self.__AddCell(meth, bound=True, border=1, align='left')
                first = True
            drow += self.__AddCell(meth, align='left')

        drow += '</table>>'
        return drow
        
    def __AddCell(self,name,align="center",bound=False,border=0,bgcolor='transparent',width=None,height=None,port=None,style=None):
        cell = f'<tr><td border="{border}" align="{align}" bgcolor="{bgcolor}" '
        if style != None:
            cell += f'style="{style}" ' 
        if bound:
            cell += f'sides="t" '
        if width != None:
            cell += f'width="{width}"'
        if height != None:
            cell += f'height="{height}"'
        cell += f'>{name}</td></tr>'
        return cell
