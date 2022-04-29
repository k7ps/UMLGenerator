from object_class import *


class Parser:
    def Parse(self, readed_code):
        pass


class PyParser(Parser):           
    def __init__(self):
        self.__initDef = "__init__"
        self.__funcDef = "def "
        self.__indicator = "#@UML"
        self.__aggrIndicator = "aggr"
        self.__compIndicator = "comp"
        self.__varDef = "self."

    def __DeleteSpaces(self, s):
        return s.replace(' ','')

    def __CalculateTab(self, start_str):
        for i in range(len(start_str)):
            if start_str[i] != ' ':
                return i
        return 0

    def __ReadName(self, start_str):
        parents_str = self.__DeleteSpaces(start_str)
        parents = []
        haveParents = True
        if parents_str.find('(') == -1 or parents_str.find('(') > parents_str.find(':'):
            haveParents = False
        parents = parents_str.split(sep = '(')
        name = parents[0][5:]
        parents_str = parents[-1].split(sep=')')[0]
        parents = parents_str.split(sep=',')
        if not haveParents:
            parents = []
        return name.split(sep=':')[0], parents

    def __ReadVariable(self, start_str):
        var_str = self.__DeleteSpaces(start_str)
        if var_str[:5] == "self.":
            var_str = var_str[5:]
        name = ''
        type = ''
        for i in range(len(var_str)):
            if var_str[i] in [':','=','+','/','-','*','%']:
                if var_str[i] == ':':
                    type = var_str[i+1:].split(sep='=')[0]
                break
            name += var_str[i]
        type = type.split(sep='.')[-1]
        if var_str.find(self.__indicator) != -1:
            end = var_str[-4:].lower()
            if end == self.__aggrIndicator or end[-1] == self.__aggrIndicator[0]:
                return name, '', type
            return name, type, ''
        return name, type, ''
            

    def __IsInit(self, start_str):
        init_str = self.__DeleteSpaces(start_str)
        return len(init_str) > 11 and init_str[3:11] == self.__initDef

    def __ReadInit(self, code, ind, size, tab):
        name = self.__initDef+'()'
        vars = []
        comps = {}
        aggrs = {}
        while ind < size and code[ind][:2*tab] == ' '*2*tab:
            var_str = self.__DeleteSpaces(code[ind])
            if len(var_str)>5 and var_str[:5] == self.__varDef:
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

    def Parse(self, readed_code):
        class_list = []
        tab = 4
        k = 0 
        while tab == 0 and k < len(readed_code):
            tab = self.__CalculateTab(readed_code[k])
            k += 1
        for i in range(len(readed_code)):
            if readed_code[i][:5] == 'class':
                name, parents = self.__ReadName(readed_code[i])
                fields = []
                compositions = {}
                aggregations = {}
                clusters = []
                for j in range(i + 1, len(readed_code)):
                    code_str = readed_code[j]
                    if code_str[:tab] == ' ' * tab:
                        if code_str[tab:tab+len(self.__funcDef)] == self.__funcDef:
                            if self.__IsInit(code_str):
                                initName, vars, comps, aggrs = self.__ReadInit(readed_code, j+1, len(readed_code), tab)
                                fields.append(initName)
                                fields += vars
                                compositions.update(comps)
                                aggregations.update(aggrs)
                            else:
                                fields.append(self.__ReadMethod(code_str))
                        elif code_str[tab] != ' ' and code_str[tab] != '#':
                            var_name, composition, aggregation = self.__ReadVariable(code_str)
                            fields.append(var_name)
                            if composition != '':
                                compositions[composition] = var_name
                            if aggregation != '':
                                aggregations[aggregation] = var_name
                    else:
                        fields = list(set(fields))
                        class_list.append(ObjectClass(name, fields, ClassInteraction(parents, compositions, aggregations, clusters)))
                        break
        return class_list


# b = PyParser()
# c = b.Parse(a)
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
