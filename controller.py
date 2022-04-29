from object_class import *
from engine import *
from settings import *
from ui import *

class Controller:
    def __init__(self):
        self.__engine = Engine() 
        self.__ui = UI()

    def Start(self):
        Set.SetStandartTheme()
        self.__engine.Read()
        self.__ui.SetClasses( self.__engine.GetClasses() )
        self.__ui.DrawUML()
