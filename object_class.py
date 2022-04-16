import settings as s

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



class ObjectClass:
    def __init__(self, name, variables, methods, interactions):
        self.__name = name
        self.__vars = variables
        self.__methods = methods
        self.__interactions = interactions

    def __init__(self, name, variables, methods, parents, compositions):
        self.__name = name
        self.__vars = variables
        self.__methods = methods
        self.__interactions = ClassInteraction(parents, compositions, {}, [])

    def Print(self):
        print('>', self.__name)
        print('\tVariables:',*self.__vars, sep='  ')
        print('\tMethods:', *self.__methods, sep='  ')
        print('\tParents:', *self.__parents, sep='  ')
        print('\tCompositions:', *self.__compositions, sep='  ')

    def Get(self):
        return (self.__name, self.__vars, self.__methods)

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
