from object_class import *
from formator import *
from settings import *
#from reader import *


class Parser:
    def Parse(self, readed_code):
        pass


class PyParser(Parser):           
    def __init__(self):
        self.__initDef = "__init__"
        self.__funcDef = "def "
        self.__classDef = "class "
        self.__indicator = Set.pyUmlSign 
        self.__aggrIndicator = Set.pyAggrSign
        self.__clustIndicator = Set.pyClustSign
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
        compositions, aggregations = {}, {}
        if start > 0:
            clusters = self.__ReadClusters(code[start-1])
        for i in range(start+1, len(code)):
            line = code[i]
            if line.startswith (tabSpace):
                line = line[tab:]
                if self.__IsMethod(line):
                    if self.__IsInit (line):
                        initName, vars, comps, aggrs = self.__ReadInit(code, i+1, tab)
                        fields.append(initName)
                        fields += vars
                        compositions.update(comps)
                        aggregations.update(aggrs)
                    else:
                        fields.append(self.__ReadMethod(line))
                elif self.__IsVar(line):
                    var_name, composition, aggregation = self.__ReadVariable(line)
                    fields.append(var_name)
                    if composition != '':
                        compositions[composition] = var_name
                    if aggregation != '':
                        aggregations[aggregation] = var_name
            else:
                break
        fields = list(set(fields))
        return ObjectClass(name, fields, ClassInteraction(parents, compositions, aggregations, clusters))

    def __ReadClusters(self, line):
        clustList = line.split(sep=' ')
        if len(clustList) < 3 or clustList[0] != self.__indicator or clustList[1] != self.__clustIndicator:
            return []
        clusters = ''.join(clustList[2:])
        if clusters.find(',') == -1:
            return clusters.split(sep=' ')
        self.__DeleteSpaces(clusters)
        return clusters.split(sep=',')

    def __IsVar(self, line):
        return (line[0].isalpha() or line[0]=='_') and line.find('=') != -1

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

    def __ReadVariable(self, start_str):
        var_str = self.__DeleteSpaces(start_str)
        if var_str.startswith(self.__varDef):
            var_str = var_str[len(self.__varDef):]
        name = ''
        type = ''
        for i in range(len(var_str)):
            if var_str[i] in [':','=','+','/','-','*','%']:
                if var_str[i] == ':':
                    type = var_str[i+1:].split(sep='=')[0]
                break
            name += var_str[i]
        type = type.split(sep='.')[-1]
        umlIndicatorInd = var_str.find(self.__indicator)
        if umlIndicatorInd != -1:
            end = var_str[umlIndicatorInd + len(self.__indicator):].lower()
            if self.__aggrIndicator.startswith(end):
                return name, '', type
            return name, type, ''
        return name, type, ''
            
    def __IsInit(self, start_str):
        init_str = self.__DeleteSpaces(start_str)[len(self.__funcDef)-1:]
        return init_str.startswith(self.__initDef)

    def __ReadInit(self, code, ind, tab):
        name = self.__initDef+'()'
        vars = []
        comps = {}
        aggrs = {}
        while ind < len(code) and code[ind].startswith(' '*2*tab):
            var_str = self.__DeleteSpaces(code[ind])
            if var_str.startswith(self.__varDef):
                varName, comp, aggr = self.__ReadVariable(code[ind])
                vars.append(varName)
                if comp != '':
                    comps[varName] = comp
                if aggr != '':
                    aggrs[varName] = aggr
            ind+=1
        return name, vars, comps, aggrs

    def __ReadMethod(self, start_str):
        method_str = self.__DeleteSpaces(start_str)
        method_str = method_str[len(self.__funcDef)-1:]
        return method_str.split(sep='(')[0]+'()'



#r = LocReader('testclass.py')
#code = r.ReadFrom()
#b = PyParser()
#c = b.Parse(code)
# print(c)
#b = PyParser()
# c = b._PyParser__ReadName("class Parser(Parser,Ashdhkasdjkasdjkasd,OK):")
#c = b._PyParser__ReadVariable("        self.a:B = a  #!UML A")
# c = b._PyParser__ReadMethod('  def aefaf(ok = "__init__"):')
# c = b._PyParser__ReadInit([' def __init__(a,b,c,d=","):'],0)
# print(c)




# for i in range(len(a)):
#     b,c = GetCompositions(a[i])
#     print(b, '-----', c)

# def __init__ (a: int):
#     self.b: int = a # !aggregation
