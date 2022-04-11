import file as f

class Engine:
    def __init__(self, paths=['test_code.py']):
        self.__paths = paths
        self.__files = []
        for path in self.__paths:
            self.__files.append(f.PyLocFile(path))

    def Read(self):
        for file in self.__files:
            file.Read()

    def GetClasses(self):
        classes = []
        for file in self.__files:
            for cl in file.GetClasses():
                classes.append(cl)
        return classes
