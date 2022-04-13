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
        for cl in self.__classes:
            self.__uml.node(cl.GetName(), self.__drawer.Draw(*cl.Get(), cl.GetComps()), shape='plaintext')
        
        for cl in self.__classes:
            for p in cl.GetParents():
                self.__uml.edge(p, cl.GetName())

            cs = cl.GetComps()
            key = 1
            for var in cl.GetVars():
                if cs.get(var) != None:
                    self.__uml.edge(cs[var],f'{cl.GetName()}:f{key}',arrowhead='onormal')
                    key += 1
                    
        self.__uml.render('uml', view=True) 
        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uml')
        os.remove(path)

