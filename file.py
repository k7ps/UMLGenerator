from object_class import *
from parser import *
from reader import *

class File:
    def __init__(self):
        self._classes: ObjectClass = []

    def GetClasses(self):
        return self._classes

class PyLocFile(File, LocReader, PyParser):
    def __init__(self, path):
        LocReader.__init__(self, path, 'utf-8')
        File.__init__(self)
        PyParser.__init__(self)

    def Read(self):
        self._classes = self.Parse(self.ReadFrom())

    


        
    
