import settings as s

class ClDrawer:
    def Draw(self, name, vs, ms, cs):
        pass

class HtmlClDrawer(ClDrawer):
    def __init__(self):
        pass

    def Draw(self, name, vs, ms, cs):
        drow = '<<table border="1" style="rounded">'
        drow += self.__AddCell(name, bgcolor="yellow", style="rounded", height=25)

        if len(vs) == 0:
            drow += self.__AddCell('', height=5)
        key = 1
        for var in vs:
            if cs.get(var) == None:
                drow += self.__AddCell(var, align='left')
            else:
                drow += self.__AddCell(var, align='left',port=f'f{key}')
                key+=1

        first = True
        if len(ms) == 0:
            drow += self.__AddCell('', bound=True, height=10, border=1)
        for meth in ms:
            if first:
                drow += self.__AddCell(meth, align='left', bound=True, border=1)
                first = False
            else:
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
        if port != None:
            cell += f'port="{port}" '
        cell += f'>{name}</td></tr>'
        return cell
