import settings as s
import object_class as o
import drawer as dr
import graphviz as gv
import os

class UI:
    def __init__(self):
        self.__classes = []
        self.__drawer = dr.HtmlClDrawer()
        self.__fileName = 'uml'
        self.__uml = gv.Digraph(self.__fileName, format='png')

    def SetClasses(self, classes):
        self.__classes = classes
        # for c in classes:
        #    c.Print()

    def DrawUML(self):
        for cl in self.__classes:
            self.__DrawClassInClust (*cl.Get(), cl.GetCompositions(), cl.GetAggregations(), cl.GetClusters())
            self.__DrawInheritances (cl.GetName(), cl.GetParents())
            self.__DrawCompositions (cl.GetName(), cl.GetCompositions())
            self.__DrawAggregations (cl.GetName(), cl.GetAggregations())

        self.__uml.render ('uml', view=True) 
        self.__RemoveFile (self.__fileName)
        
    def __DrawClassInClust(self, className, fields, compositions, aggregations, clusters, graph=None, ind=0):
        if graph == None:
            graph = self.__uml

        if ind == len(clusters):
            self.__DrawClass (className, fields, compositions, aggregations, graph)
        else:
            with graph.subgraph (name=f'cluster{clusters[ind]}') as subgr:
                subgr.attr(label=clusters[ind], style='rounded,filled', color='lightgrey')
                self.__DrawClassInClust (className, fields, compositions, aggregations, clusters, subgr, ind+1)

    def __DrawClass(self, className, fields, compositions, aggregations, graph):
        graph.node(className, self.__drawer.Draw(className, fields, compositions, aggregations), shape='plaintext')

    def __DrawInheritances(self, className, parents):
        for parent in parents:
            self.__uml.edge(parent, className, arrowhead='onormal')

    def __DrawCompositions(self, className, compositions):
        for var in compositions:
            self.__uml.edge(compositions[var], f'{className}:{var}', arrowhead='diamond')

    def __DrawAggregations(self, className, aggregations):
        for var in aggregations:
            self.__uml.edge(aggregations[var], f'{className}:{var}', arrowhead='odiamond')

    def __RemoveFile(self, fileName):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), fileName)
        os.remove(path)

