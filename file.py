from object_class import *
from parser import *
from reader import *

class File:
    def __init__(self):
        self._lastChangeDate = self.GetChangeDate()
        self._classes = []

    def GetChangeDate(self):
        return 2
    
    def GetClasses(self):
        return self._classes

class PyLocFile(File, LocReader, PyParser):
    def __init__(self, path):
        File.__init__(self)
        LocReader.__init__(self, path, 'utf-8')
        PyParser.__init__(self)

    def Read(self):
        self._classes = self.Parse(self.ReadFrom())

    


        
    
