
class Reader:
    def __init__(self, enc='utf8'):
        self.__encode = enc

    def ReadCode(self, path):
        readed_code = []
        with open(path, encoding=self.__encode) as f:
            for i in f:
                readed_code.append(i) # прочитали весь код построчно
        return readed_code