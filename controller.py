import object_class as o
import engine as e
import settings as s
import ui

class Controller:
    def __init__(self):
        self.__engine = e.Engine() 
        self.__ui = ui.UI()

    def Start(self):
        s.Set.SetStandartTheme()
        self.__engine.Read()
        self.__ui.SetClasses( self.__engine.GetClasses() )
        self.__ui.DrawUML()
