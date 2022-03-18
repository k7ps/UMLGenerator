import object_class as o
import engine as e
import ui as u

class Controller:
    def __init__(self):
        self.__engine = e.Engine() 
        self.__ui = u.UI()

    def Start(self):
        self.__engine.Read()
        self.__ui.SetClasses( self.__engine.GetClasses() )
        self.__ui.DrawUML()
