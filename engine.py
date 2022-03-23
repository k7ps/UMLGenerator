import object_class as o
import reader as r
import parser as p

class Engine:
    def __init__(self):
        self.__classes = []
        self.__reader = r.Reader()
        self.__parser = p.Parser()
        self.__path = 'test_code.py'

    def Read(self):
        readed_file = self.__reader.ReadCode(self.__path)
        self.__classes = self.__parser.FindClasses(readed_file)

    def GetClasses(self):
        return self.__classes
