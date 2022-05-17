from enum import Enum

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



class Drawable:
    def __init__(self, ignored):
        self.__IsIgnore = ignored

    @property
    def IsIgnore(self):
        return self.__IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, ignored):
        self.__IsIgnore = ignored


class AccessMod(Enum):
    PUBLIC = 0
    PROTECTED = 1
    PRIVATE = 2


class Field(Drawable):
    def __init__(self, name, ignored):
        super().__init__(ignored)
        self.__name = name

        self.__modifier = AccessMod.PUBLIC
        if name.startswith('__'):
            self.__modifier = AccessMod.PRIVATE
        elif name.startswith('_'):
            self.__modifier = AccessMod.PROTECTED

    @property
    def modifier(self):
        return self.__modifier

    @property
    def name(self):
        return self.__name

    def IsVariable(self):
        return type(self) is Variable

    def IsMethod(self):
        return type(self) is Method


    def __repr__(self):
        return "Field(%s, %s)" % (self.name, self.modifier)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())


class Variable(Field):
    def __init__(self, name, ignored=False):
        super().__init__(name, ignored)


class Method(Field):
    def __init__(self, name, ignored=False):
        super().__init__(name, ignored)


class ObjectClass(Drawable):
    def __init__(self, name, fields, interactions, ignored=False):
        super().__init__(ignored)
        self.__name = name
        self.__fields = fields

        #self.__fields.sort()
        self.__interactions: ClassInteraction = interactions

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
        print('\tFields:',[i.name for i in self.__fields], sep=',')
        print('\tParents:', *self.GetParents(), sep='  ')
        print('\tCompositions:', self.GetCompositions(), sep='  ')
        print('\tAggregations:', self.GetAggregations(), sep='  ')
        print('\tClusters:', *self.GetClusters(), sep='  ')
