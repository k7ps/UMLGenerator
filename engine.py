from file import *
from object_class import *

class Engine:
    def __init__(self, paths=[]):
        self.__paths = paths
        self.__files: File = []
        for path in self.__paths:
            self.__files.append(PyLocFile(path))
    
    def Read(self):
        for file in self.__files:
            file.ReadClasses()

    @property
    def classes(self):
        classes = []
        for file in self.__files:
            classes += file.GetClasses()
        return classes
