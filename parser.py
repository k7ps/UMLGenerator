from object_class import *
from formator import *
from settings import *
from modchecker import *


#@UML clusters Parsing
class Parser:
    def Parse(self, readed_code):
        pass


#@UML clusters Parsing
class PyParser(Parser):           
    def __init__(self):
        self.__initDef = "__init__"
        self.__funcDef = "def"
        self.__classDef = "class "
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
        if start > 0:
            clusters, ignored = ModificationChecker.ReadClass(code[start-1])
        for i in range(start+1, len(code)):
            line = code[i]
            if line.startswith (tabSpace):
                line = line[tab:]
                if self.__IsMethod(line):
                    method = self.__ReadMethod(line)
                    fields.append (method)
                    if self.__IsInit (method.name):
                        varbls = self.__ReadInit(code, i+1, tab)
                        fields += varbls
                elif self.__IsVar(line):
                    var = self.__ReadVariable(line)
                    fields.append (var)
            else:
                break
        return ObjectClass(name, fields, ClassInteraction(parents, clusters), ignored)

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
        haveHardDef = line.find(f' {self.__funcDef} ') != -1 and not line.startswith(' ')
        return line.startswith(f'{self.__funcDef} ') or haveHardDef

    def __DeleteNamespace(self, name):
        return name.split(sep='.')[-1]

    def __ReadClassName(self, line):
        defStr = self.__DeleteSpaces(line)
        haveParents = defStr.find('(') != -1 and defStr.find('(') < defStr.find(':')
        parents = defStr.split(sep = '(')
        name = parents[0][5:]
        defStr = parents[-1].split(sep=')')[0]
        parents = defStr.split(sep=',')
        parents = [self.__DeleteNamespace(p) for p in parents]
        if not haveParents:
            parents = []
        return name.split(sep=':')[0], parents

    def __ReadType(self, typeStr):
        typeStr = self.__DeleteSpaces(typeStr)
        if typeStr.find(',') != -1:
            typeStr = typeStr.split('[')[0]
        else:
            openbr = typeStr.find('[')
            closebr = typeStr.rfind(']')
            while openbr != -1 and closebr != -1:
                typeStr = typeStr[openbr+1:closebr]
                openbr = typeStr.find('[')
                closebr = typeStr.rfind(']')
        return self.__DeleteNamespace(typeStr)

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
        return Variable(name, varType, isAggr, ignore)
            
    def __IsInit(self, name):
        return name == f'{self.__initDef}()'

    def __ReadInit(self, code, ind, tab):
        variables = []
        while ind < len(code) and code[ind].startswith(' '*2*tab):
            varStr = self.__DeleteSpaces(code[ind])
            if self.__IsVar(varStr, inInit=True):
                variables.append (self.__ReadVariable(varStr))
            ind+=1
        return variables

    def __ReadMethod(self, startStr):
        ignore = ModificationChecker.ReadMethod (startStr)
        name = ''
        words = startStr.split()
        for i, word in enumerate(words):
            if word.find('(') != -1:
                if word.startswith('('):
                    if i != 0:
                        name = words[i-1]
                    else:
                        continue
                else:
                    name = word.split(sep='(')[0]
                break
        return Method (name, ignore)

#p = PyParser()
#st = 'def __init__(asdasd):'
#print(p._PyParser__IsInit(st))
#print(p._PyParser__ReadMethod(st).name)
