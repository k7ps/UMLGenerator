#@UML clusters Reading
class Reader:
    def __init__(self, path, enc='utf-8'):
        self._path = path
        self._encode = enc

    def ReadCode(self):
        pass


#@UML clusters Reading
class LocReader(Reader):
    def __init__(self, path, enc='utf-8'):
        super().__init__(path, enc=enc)

    def ReadCode(self):
        readed_code = []
        with open(self._path, encoding=self._encode) as f:
            for i in f:
                readed_code.append(i)
        return readed_code

