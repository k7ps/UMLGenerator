#@UML clusters Reading
class Reader:
    def __init__(self, path, enc='utf-8'):
        self._path = path
        self._encode = enc

    def ReadFrom(self):
        pass


#@UML clusters Reading
class LocReader(Reader):
    def __init__(self, path, enc='utf-8'):
        super().__init__(path, enc=enc)

    def ReadFrom(self):
        readed_code = []
        with open(self._path, encoding=self._encode) as f:
            for i in f:
                readed_code.append(i) # прочитали весь код построчно
        return readed_code

