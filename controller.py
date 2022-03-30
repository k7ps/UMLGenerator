import object_class as o
import engine as e
import ui

class Controller:
    def __init__(self):
        self.__engine = e.Engine() 
        self.__ui = ui.UI()

    def Start(self):
        self.__engine.Read()
        self.__ui.SetClasses( self.__engine.GetClasses() )
        self.__ui.DrawUML()
