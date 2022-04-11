import object_class
import parser as p
import reader as r

class File:
    def __init__(self):
        self._lastChangeDate = self.GetChangeDate()
        self._classes = []

    def GetChangeDate(self):
        return 2
    
    def GetClasses(self):
        return self._classes

class PyLocFile(File, r.LocReader, p.PyParser):
    def __init__(self, path):
        File.__init__(self)
        r.LocReader.__init__(self, path, 'utf-8')
        p.PyParser.__init__(self)

    def Read(self):
        self._classes = self.Parse(self.ReadFrom())

    


        
    
