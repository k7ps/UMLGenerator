from object_class import *
from engine import *
from settings import *
from userset import *
from ui import *


class Controller:
    def __init__(self):
        self.__userSet: UserSettings = UserSettings()
        self.__userSet.Read()

        self.__engine: Engine = Engine(self.__GetPaths()) 
        self.__ui: UI = UI()
    
    def __GetPaths(self):
        paths = self.__userSet.files
        curDir = os.path.abspath(os.curdir)
        if len(paths) == 0:
            paths = self.__FindAllPaths(curDir)
        else:
            for i in range(len(paths)):
                paths[i] = os.path.join(curDir, paths[i])

        for ignorePath in self.__userSet.ignoreFiles:
            ignorePath = os.path.join(curDir, ignorePath)
            if ignorePath in paths:
                paths.remove(ignorePath)

        return paths

    def __FindAllPaths(self, curDir):
        paths = []
        if Set.readOnlyThisDirFiles:
            for file in os.listdir(curDir):
                if file.endswith(".py"):
                    paths.append(os.path.join(curDir, file))
        else:
            for root, dirs, files in os.walk(curDir):
                for file in files:
                    if file.endswith(".py"):
                        paths.append(os.path.join(root, file))
        return paths

    def Start(self):
        self.__engine.Read()
        self.__ui.SetClasses( self.__engine.GetClasses() )
        self.__ui.DrawUML()
