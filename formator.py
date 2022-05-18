from settings import *

#@UML clusters Parsing
class Formator:
    _comSign = ''
    _umlSign = ''

    def FormatCode(code):
        pass


#@UML clusters Parsing
class PyFormator(Formator):
    _comSign = '#'
    _umlSign = Set.pyUmlSign

    def FormatCode(code):
        formatted_code = code[:]
        PyFormator.__DeleteComments (formatted_code)
        PyFormator.__DeleteEmptyLines (formatted_code)
        PyFormator.__CombineSepLines (formatted_code)
        return formatted_code

    def __DeleteComments(code):
        for i in range(len(code)):
            com = -1
            for j in range(len(code[i])):
                if code[i].startswith(PyFormator._comSign, j) and not code[i].startswith(PyFormator._umlSign, j):
                    com = j
                    break
            if com != -1:
                code[i] = code[i][:com]
            elif len(code[i]) > 0 and code[i][-1:] == '\n':
                code[i] = code[i][:-1]

    def __DeleteEmptyLines(code):
        i = 0
        while i < len(code):
            if code[i].isspace() or len(code[i])==0:
                code.pop(i)
            else:
                i += 1

    def __CombineSepLines(code):
        stack = []
        opnBrkt = ['(','[','{','"""',"'''"]
        clsBrkt = {'(':')','[':']','{':'}','"""':'"""',"'''":"'''"}
        i = 0
        while i < len(code):
            toInd = i
            for j in range(len(code[i])):
                if code[i][j] in opnBrkt: 
                    stack.append((code[i][j],i))
                elif len(code[i])-j>=3 and code[i][j:j+3] in opnBrkt and (len(stack)==0 or code[i][j:j+3] != stack[-1][0]):
                    stack.append((code[i][j:j+3],i))
                elif len(stack)>0:
                    if code[i][j] == clsBrkt[stack[-1][0]]:
                        toInd = stack.pop()[1]
                    elif len(code[i])-j>=3 and code[i][j:j+3] == clsBrkt[stack[-1][0]]:
                        toInd = stack.pop()[1]
            while i != toInd:
                code[i-1] += code.pop(i)
                i -= 1
            i += 1
