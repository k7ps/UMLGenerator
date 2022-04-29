from settings import *
from object_class import *
from drawer import *

import graphviz as gv
import os

class UI:
    def __init__(self):
        self.__classes = []
        self.__drawer = HtmlClDrawer()
        self.__fileName = 'uml'
        self.__uml = gv.Digraph (self.__fileName, format=Set.imgFormat)
        self.__uml.attr (fontname=Set.clustFont)
        self.__clusterSize = {}

    def SetClasses(self, classes):
        self.__classes = classes
        #for c in classes:
        #   c.Print()

    def DrawUML(self):
        self.__CountClustersSize(self.__classes)

        for cl in self.__classes:
            self.__SortClusters (cl)
            self.__DrawClassInClust (*cl.Get(), cl.GetCompositions(), cl.GetAggregations(), cl.GetClusters())
            self.__DrawInheritances (cl.GetName(), cl.GetParents())
            self.__DrawCompositions (cl.GetName(), cl.GetCompositions())
            self.__DrawAggregations (cl.GetName(), cl.GetAggregations())

        self.__uml.render (self.__fileName, view=True) 
        self.__RemoveFile (self.__fileName)
        
    def __DrawClassInClust(self, className, fields, compositions, aggregations, clusters, graph=None, ind=0):
        if graph == None:
            graph = self.__uml

        if ind == len(clusters):
            self.__DrawClass (className, fields, compositions, aggregations, graph)
        else:
            with graph.subgraph (name=f'cluster{clusters[ind]}') as subgr:
                subgr.attr(label=clusters[ind], style=Set.clustStyle, color=Set.clustCol)
                self.__DrawClassInClust (className, fields, compositions, aggregations, clusters, subgr, ind+1)

    def __DrawClass(self, className, fields, compositions, aggregations, graph):
        graph.node(className, self.__drawer.Draw(className, fields, compositions, aggregations), 
                    shape='plaintext', fontname=Set.clFont)

    def __DrawInheritances(self, className, parents):
        for parent in parents:
            self.__uml.edge(parent, className, arrowhead=Set.inherStyle, color=Set.arrowCol)

    def __DrawCompositions(self, className, compositions):
        for var in compositions:
            self.__uml.edge(compositions[var], f'{className}:{var}', arrowhead=Set.compStyle, color=Set.arrowCol)

    def __DrawAggregations(self, className, aggregations):
        for var in aggregations:
            self.__uml.edge(aggregations[var], f'{className}:{var}', arrowhead=Set.aggrStyle, color=Set.arrowCol)

    def __CountClustersSize(self, classes):
        for cl in classes:
            for cluster in cl.GetClusters():
                if self.__clusterSize.get(cluster) == None:
                    self.__clusterSize[cluster] = 1
                else:
                    self.__clusterSize[cluster] += 1

    def __SortClusters(self, objClass):
        clusters = objClass.GetClusters()
        if not self.__IsClustersSorted (clusters):
            c = [(self.__clusterSize[cl], cl) for cl in clusters]
            c.sort(reverse=True)
            clusters = [p[1] for p in c]
            objClass.SetClusters (clusters)

    def __IsClustersSorted(self, clusters):
        if len(clusters) == 0:
            return True;
        for i in range(1,len(clusters)):
            if self.__clusterSize[clusters[i]] > self.__clusterSize[clusters[i-1]]:
                return False
        return True

    def __RemoveFile(self, fileName):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), fileName)
        os.remove(path)

