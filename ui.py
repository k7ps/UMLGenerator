import settings as s
import object_class as o
import drawer as dr
import graphviz as gv
import os

class UI:
    def __init__(self):
        self.__classes = []
        self.__drawer = dr.HtmlClDrawer()
        self.__uml = gv.Digraph('uml', format='png')

    def SetClasses(self, classes):
        self.__classes = classes
        # for c in classes:
        #    c.Print()

    def DrawUML(self):
        cod = 'A'
        for cl in self.__classes:
            self.__uml.node(cod, cl.Draw(self.__drawer), shape='plaintext')
            cod = chr(ord(cod)+1)
        
        self.__uml.render('uml', view=True) 
        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uml')
        os.remove(path)

