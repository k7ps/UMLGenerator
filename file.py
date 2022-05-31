from os import path

from object_class import *
from parser import *
from reader import *

class File:
    def __init__(self):
        self._classes: ObjectClass = []

    def GetClasses(self):
        return self._classes

    def ReadClasses(self):
        pass

class PyLocFile(File, LocReader, PyParser):
    def __init__(self, path):
        LocReader.__init__(self, path, 'utf-8')
        File.__init__(self)
        PyParser.__init__(self)
    
    def ReadClasses(self):
        self._classes = self.Parse(self.ReadCode())

        fileName = path.basename(self._path)
        fileName = path.splitext(fileName)[0]
        for i in range(len(self._classes)):
            self._classes[i].SetFileName (fileName) 
