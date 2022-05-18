from object_class import *
from formator import *
from settings import *
from modchecker import *

from reader import * 


#@UML clusters Parsing
class Parser:
    def Parse(self, readed_code):
        pass


#@UML clusters Parsing
class PyParser(Parser):           
    def __init__(self):
        self.__initDef = "__init__"
        self.__funcDef = "def "
        self.__classDef = "class "
        self.__listDef = "list"
        self.__varDef = "self."
        self.__standardTab = 4

    def Parse(self, readed_code):
        code = self.__FormatCode (readed_code)
        tab = self.__CalculateTab (code)
        self.__TabToSpaces (code, tab)
        classes = []

        for i in range(len(code)):
            if code[i].startswith (self.__classDef):
                classes.append (self.__ReadClass(code, i, tab))

        return classes

    def __FormatCode(self, readed_code):
        return PyFormator.FormatCode(readed_code)

    def __CalculateTab(self, code):
        tab = 0
        for i, line in enumerate(code):
            if line.startswith (self.__classDef):
                tab = self.__CalculateTabStr (code[i+1])
                if tab != 0:
                    break
        return tab if tab != 0 else self.__standardTab

    def __CalculateTabStr(self, start_str):
        for i in range(len(start_str)):
            if start_str[i] != ' ':
                return i
        return 0

    def __TabToSpaces(self, code, tab):
        for i in range(len(code)):
            code[i].replace('\t', ' '*tab)

    def __DeleteSpaces(self, s):
        return s.replace(' ','')
    
    def __ReadClass(self, code, start, tab):
        tabSpace = ' ' * tab
        name, parents = self.__ReadClassName (code[start])
        fields, clusters = [], []
        ignored = False
        #compositions, aggregations = {}, {}
        if start > 0:
            clusters, ignored = ModificationChecker.ReadClass(code[start-1])
        for i in range(start+1, len(code)):
            line = code[i]
            if line.startswith (tabSpace):
                line = line[tab:]
                if self.__IsMethod(line):
                    if self.__IsInit (line):
                        init, varbls = self.__ReadInit(code, i+1, tab)
                        fields.append (init)
                        fields += varbls
                        #compositions.update(comps)
                        #aggregations.update(aggrs)
                    else:
                        fields.append (self.__ReadMethod(line))
                elif self.__IsVar(line):
                    var = self.__ReadVariable(line)
                    fields.append (var)
                    #if composition != '':
                    #    compositions[composition] = var.name
                    #if aggregation != '':
                    #    aggregations[aggregation] = var.name
            else:
                break
        #for field in fields:
        #    print(field.name, sep=' ')
        #print
        fields = list(set(fields))
        return ObjectClass(name, fields, ClassInteraction(parents, clusters), ignored)

    #def __ReadClusters(self, line):
    #    clustList = line.split(sep=' ')
    #    if len(clustList) < 3 or clustList[0] != self.__indicator or clustList[1] != self.__clustIndicator:
    #        return []
    #    clusters = ''.join(clustList[2:])
    #    if clusters.find(',') == -1:
    #        return clusters.split(sep=' ')
    #    self.__DeleteSpaces(clusters)
    #    return clusters.split(sep=',')

    def __IsLetterName(self, c):
        return self.__IsFirstLetter(c) or c.isdigit()

    def __IsFirstLetter(self, c):
        return c.isalpha() or c == '_'

    def __IsVar(self, line, inInit=False):
        if line.find('=') == -1:
            return False

        if inInit:
            line = self.__DeleteSpaces(line)
            if not line.startswith(self.__varDef):
                return False
            line = line[len(self.__varDef):]
        else:
            if not self.__IsFirstLetter(line[0]):
                return False
            line = self.__DeleteSpaces(line)

        for i, c in enumerate(line):
            if not self.__IsLetterName(c):
                return c == '=' or c == ':'
        return False

    def __IsMethod(self, line):
        return line.startswith (self.__funcDef)

    def __ReadClassName(self, line):
        defStr = self.__DeleteSpaces(line)
        haveParents = defStr.find('(') != -1 and defStr.find('(') < defStr.find(':')
        parents = defStr.split(sep = '(')
        name = parents[0][5:]
        defStr = parents[-1].split(sep=')')[0]
        parents = defStr.split(sep=',')
        if not haveParents:
            parents = []
        return name.split(sep=':')[0], parents

    def __ReadType(self, typeStr):
        typeStr = self.__DeleteSpaces(typeStr)
        while typeStr.startswith(self.__listDef):
            typeStr = typeStr[len(self.__listDef):]
            if typeStr.startswith('['):
                typeStr = typeStr[1:]
            if typeStr.endswith(']'):
                typeStr = typeStr[:-1]
        return typeStr.split(sep='.')[-1]

    def __ReadVariable(self, line):
        varStr = self.__DeleteSpaces(line)
        if varStr.startswith(self.__varDef):
            varStr = varStr[len(self.__varDef):]
        name = ''
        varType = ''
        isAggr, ignore = ModificationChecker.ReadVariable(line)
        for i, c in enumerate(varStr):
            if not self.__IsLetterName(c):
                if c == ':':
                    varType = varStr[i+1:].split(sep='=')[0]
                break
            name += c
        varType = self.__ReadType(varType)
        #print(name, varType, isAggr, ignore)
        return Variable(name, varType, isAggr, ignore)
            
    def __IsInit(self, start_str):
        init_str = self.__DeleteSpaces(start_str)[len(self.__funcDef)-1:]
        return init_str.startswith(self.__initDef)

    def __ReadInit(self, code, ind, tab):
        init = self.__ReadMethod(code[ind-1])
        variables = []
        while ind < len(code) and code[ind].startswith(' '*2*tab):
            varStr = self.__DeleteSpaces(code[ind])
            if self.__IsVar(varStr, inInit=True):
                variables.append (self.__ReadVariable(varStr))
            ind+=1
        return init, variables

    def __ReadMethod(self, startStr):
        ignore = ModificationChecker.ReadMethod (startStr)
        method_str = self.__DeleteSpaces (startStr)
        method_str = method_str[len(self.__funcDef)-1:]
        return Method( method_str.split(sep='(')[0]+'()', ignore )


#p = PyParser()
#l = LocReader('test_code.py')
#code = l.ReadFrom()
#c = p._PyParser__ReadVariable('     self.__asd:  list[obj.ok] = asda sda sd #@UML aggr; ignore')
#c = p._PyParser__ReadMethod(' def    okokok(asd a,ads, asd asd):  #@UML aggr; ignore')
#pcode = p.Parse(code)
#for cl in pcode:
   # cl.Print()
