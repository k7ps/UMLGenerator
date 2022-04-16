import object_class as o

class Parser:
    def Parse(self, readed_code):
        pass



class PyParser(Parser):
    def __init__(self):
        pass
    
    def __ReadName(self, start_str):
        name = None
        parents = []
        parent_start = None
        parent_end = None
        name_end = None
        for i in range(len(start_str)):
            if start_str[i] == ':':
                if name_end == None:
                    name_end = i
                break
            if start_str[i] == '(':
                name_end = i
                parent_start = i + 1
            if start_str[i] == ')':
                parent_end = i
        if parent_start != None:
            parents = start_str[parent_start:parent_end].split()
        name = start_str[6:name_end]
        return name, parents

    def __ReadMethods(self, start_str):
        name_start = 8 # First letter in name
        name_end = None
        for i in range(len(start_str)):
            if start_str[i] == '(':
                name_end = i
                break
        method_name = start_str[name_start:name_end]
        return method_name

    def __ReadVariables(self, start_str):
        name_start = 4 # First letter in name
        name_end = None
        for i in range(len(start_str)):
            if start_str[i] == '=':
                name_end = i
                break
        variable_name = start_str[name_start:name_end]
        return variable_name

    def Parse(self, readed_code):
        class_list = []
        for i in range(len(readed_code)):
            if readed_code[i][:5] == 'class':
                nm, ps = self.__ReadName(readed_code[i])
                ms = []
                vs = []
                cs = {}
                for j in range(i + 1, len(readed_code)):
                    if readed_code[j][:4] == '    ':
                        if readed_code[j][4:8] == 'def ':
                            ms.append(self.__ReadMethods(readed_code[j]))
                        elif readed_code[j][4] != ' ' and readed_code[j][4] != '#':
                            vs.append(self.__ReadVariables(readed_code[j]))
                    else:
                        class_list.append(o.ObjectClass(nm, vs+ms, o.ClassInteraction(ps, cs,{},[])))
                        break
        return class_list

# read = r.Reader()
# a = read.read_code(path)
# b = Parser.FindClasses(a)
# for i in range(5):
#     print(b[i].Print())
