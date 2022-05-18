from object_class import *
from engine import *
from settings import *
from ui import *

paths = ['main.py','controller.py','engine.py','ui.py','drawer.py','file.py','formator.py',
         'object_class.py', 'reader.py', 'settings.py','parser.py', 'modchecker.py']
#paths = ['test_code2.py']

class Controller:
    def __init__(self):
        self.__engine: Engine = Engine(paths) 
        self.__ui: UI = UI()

    def Start(self):
        Set.SetStandartTheme()
        self.__engine.Read()
        self.__ui.SetClasses( self.__engine.GetClasses() )
        self.__ui.DrawUML()
