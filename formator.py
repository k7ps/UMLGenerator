import settings as s

class Formator:
    def FormatCode(code):
        pass

class PyFormator(Formator):
    __comSign = '#'

    def FormatCode(code):
        formatted_code = code[:]
        PyFormator.__DeleteComments (formatted_code)
        PyFormator.__CombineSepLines (formatted_code)
        PyFormator.__RemoveNeedless (formatted_code)
        return formatted_code

    def __DeleteComments(code):
        for i in range(len(code)):
            com = code[i].find(PyFormator.__comSign)
            if com != -1 and com != code[i].find(s.Set.umlSign):
                code[i] = code[i][:com]
            elif len(code[i]) > 0 and code[i][-1:] == '\n':
                code[i] = code[i][:-1]

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
                else:
                    if len(stack)>0:
                        if code[i][j] == clsBrkt[stack[-1][0]]:
                            toInd = stack.pop()[1]
                        elif len(code[i])-j>=3 and code[i][j:j+3] == clsBrkt[stack[-1][0]]:
                            toInd = stack.pop()[1]
            while i != toInd:
                code[i-1] += code.pop(i)
                i -= 1
            i += 1
