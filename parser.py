import inspect
import sys
import code
import obj
import copy

path = './code_example.py'

def read_code(path):
    # a = [cls_name for cls_name, cls_obj in inspect.getmembers(code) if inspect.isclass(cls_obj)]
    # return a
    a = []
    with open(path, encoding='utf8') as f:
        for i in f:
            a.append(i)#i.replace('    ', '\t')) # прочитали весь код построчно

    i = 0
    while i < len(a):   # Очистка кода от комментариев
        for j in range(len(a[i])):
            if a[i][j] == '#':
                a.pop(i)
                i -= 1
                break
        i += 1
    return a

def find_classes(a):
    b = []
    for i in range(len(a)):
        if a[i][:5] == 'class':
            name = a[i][6:]
            methods = []
            variables = []
            parents = []
            compositions = []
            for j in range(i + 1, len(a)):
                if a[j][:4] == '    ' and  a[j][4] != ' ':
                    if a[j][4:7] == 'def':
                        methods.append(a[j][8:])
                    else:
                        variables.append(a[j])
                else:
                    b.append(obj.ObjectClass(name, variables, methods, parents, compositions))
                    break

    return b
    # for i in range(len(a)):
    #     if a[i].find('class ') != -1:
    #         b.append(a[i]) # нашли классы
    # b[i] = 'class Animal' далее убираем слово class
    # c = []
    # for i in range(len(b)):
    #     temp = b[i].split(' ') 
    #     temp.pop(0)
    #     temp[0] = temp[0][:-2]
    #     c.append(temp[0])
    # return c
    # print(c) # в с хранятся названия классов 
    # for i in c:
        # print(i)
a = read_code(path)
b = find_classes(a)
for i in b:
    i.Print()
