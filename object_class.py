import settings as s

class ObjectClass:
    def __init__(self, name, variables, methods, parents, compositions):
        self.__name = name
        self.__vars = variables
        self.__methods = methods
        self.__parents = parents
        self.__compositions = compositions

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
        return self.__parents

    def GetComps(self):
        return self.__compositions

    def GetVars(self):
        return self.__vars
