class ClassInteraction:
    def __init__(self, parents, compositions, aggregations, clusters):
        self.__parents = parents
        self.__compositions = compositions
        self.__aggregations = aggregations
        self.__clusters = clusters

    def GetParents(self):
        return self.__parents

    def GetCompositions(self):
        return self.__compositions

    def GetAggregations(self):
        return self.__aggregations

    def GetClusters(self):
        return self.__clusters

    def SetClusters(self, clusters):
        self.__clusters = clusters



class ObjectClass:
    def __init__(self, name, fields, interactions):
        self.__name = name
        self.__fields = fields
        self.__fields.sort()
        self.__interactions = interactions

    def Get(self):
        return (self.__name, self.__fields)

    def GetName(self):
        return self.__name

    def GetParents(self):
        return self.__interactions.GetParents()

    def GetCompositions(self):
        return self.__interactions.GetCompositions()

    def GetAggregations(self):
        return self.__interactions.GetAggregations()

    def GetClusters(self):
        return self.__interactions.GetClusters()
    
    def SetClusters(self, clusters):
        self.__interactions.SetClusters (clusters)

    def Print(self):
        print('>', self.__name)
        print('\tFields:',*self.__fields, sep=',')
        print('\tParents:', *self.GetParents(), sep='  ')
        print('\tCompositions:', self.GetCompositions(), sep='  ')
        print('\tAggregations:', self.GetAggregations(), sep='  ')
        print('\tClusters:', *self.GetClusters(), sep='  ')
