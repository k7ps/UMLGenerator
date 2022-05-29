import graphviz as gv
import os

from settings import *
from object_class import *
from drawer import *


#@UML clusters Drawing
class UI:
    def __init__(self):
        self.__classes = []
        self.__drawer: ClassDrawer = HtmlClassDrawer()
        self.__fileName = 'uml'
        self.__uml = gv.Digraph (self.__fileName, engine='dot', format=Set.imgFormat)
        #self.__uml.attr(splines='polyline')
        self.__uml.attr (fontname=Set.clustFont)
        self.__clusterSize = {}

    def SetClasses(self, classes):
        self.__classes = classes

    def DrawUML(self):
        self.__CountClustersSize(self.__classes)

        for cl in self.__classes:
            if cl.IsIgnore:
                continue
            self.__UpdateClusters (cl)
            self.__DrawClassInClust (*cl.Get(), cl.GetClusters())
            self.__DrawInheritances (cl.GetName(), cl.GetParents())
            self.__DrawCompositions (cl.GetName(), cl.GetVars())

        self.__uml.render (self.__fileName, view=True) 
        self.__RemoveFile (self.__fileName)
        
    def __DrawClassInClust(self, className, fields, clusters, graph=None, ind=0):
        if graph == None:
            graph = self.__uml

        if ind == len(clusters):
            self.__DrawClass (className, fields, graph)
        else:
            with graph.subgraph (name=f'cluster{clusters[ind]}') as subgr:
                subgr.attr(label=clusters[ind], style=Set.clustStyle, color=Set.clustCol)
                self.__DrawClassInClust (className, fields, clusters, subgr, ind+1)

    def __DrawClass(self, className, fields, graph):
        graph.node(className, self.__drawer.Draw(className, fields), shape='plaintext', fontname=Set.clFont)

    def __IsClassDrawn(self, className):
        for cl in self.__classes:
            if cl.GetName() == className:
                return True
        return False

    def __IsNeedToDrawArrow(self, className):
        isDrawn = self.__IsClassDrawn(className)
        return isDrawn or (Set.drawUndefClasses and not isDrawn)

    def __DrawMissingClass(self, className):
        if Set.drawUndefClasses and not self.__IsClassDrawn (className):
            self.__DrawClass(className, [], self.__uml)

    def __DrawInheritances(self, className, parents):
        for parent in parents:
            if self.__IsNeedToDrawArrow(parent):
                self.__uml.edge(parent, className, arrowhead='none', arrowtail=Set.inherStyle, dir='both', color=Set.arrowCol)
                self.__DrawMissingClass(parent)

    def __DrawCompositions(self, className, variables):
        for var in variables:
            if ( var.HaveType() and not self.__IsClassIgnored(var.GetType()) and  
                    not var.IsIgnore and self.__IsNeedToDrawArrow(var.GetType()) ):
                if var.isAggr:
                    self.__uml.edge(f'{className}:{var.name}', var.GetType(), arrowhead='none',arrowtail=Set.aggrStyle, dir='both', 
                            color=Set.arrowCol)
                    #self.__uml.edge(var.GetType(), f'{className}:{var.name}', arrowhead=Set.aggrStyle, color=Set.arrowCol)
                else:
                    self.__uml.edge(f'{className}:{var.name}', var.GetType(), arrowhead='none',arrowtail=Set.compStyle, dir='both', 
                            color=Set.arrowCol)
                    #self.__uml.edge(var.GetType(), f'{className}:{var.name}', arrowhead=Set.compStyle, color=Set.arrowCol)
                self.__DrawMissingClass(var.GetType())

    def __IsClassIgnored(self, className):
        for cl in self.__classes:
            if cl.GetName() == className:
                return cl.IsIgnore

    def __CountClustersSize(self, classes):
        for cl in classes:
            if cl.IsIgnore:
                continue
            for cluster in cl.GetClusters():
                if self.__clusterSize.get(cluster) == None:
                    self.__clusterSize[cluster] = 1
                else:
                    self.__clusterSize[cluster] += 1

    def __UpdateClusters(self, objClass):
        if Set.groupByFiles:
            if not Set.drawOneFileGroup:
                cluster = objClass.GetClusters()[0]
                if self.__clusterSize[cluster] == 1:
                    objClass.SetClusters ([])
        else:
            self.__SortClusters(objClass)

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
        path = os.path.join(os.path.abspath(fileName))
        os.remove(path)

