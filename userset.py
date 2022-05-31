import json
import os

from settings import *


#@UML ignore
class JSONParsingError(Exception):
    def __init__(self, text):
        self.__text = text
    def __str__(self):
        return self.__text


class UserSettings:
    def __init__(self):
        self.__fileName = 'umlset.json'
        self.__settings = {}
        self.__files = []
        self.__ignoreFiles = []

        self.__trueSigns = ['true', '1', 'yes']
        self.__falseSigns = ['false', '0', 'no']

        self.__ignorePrv = 'ignoreprivate'
        self.__ignorePrt = 'ignoreprotected'
        self.__ignorePrvCm = 'ignoreprivatecomps'
        self.__ignorePrtCm = 'ignoreprotectedcomps'
        self.__readOnlyDir = 'readfilesonlyinthisdir'
        self.__drawUndefCl = 'drawundefinedclasses'
        self.__groupByFiles = 'groupbyfiles'
        self.__drawOneClassGroup = 'drawoneclassgroups'
        self.__removeAccessPrefix = 'removeaccessprefix'
        self.__altEngine = 'alternativeengine'
        self.__filesSign = 'files'
        self.__ignoreFilesSign = 'ignorefiles'
        self.__colorSign = 'color'

        self.__readingErrorMsg = f'Decoding {self.__fileName} error:'
        self.__parsingErrorMsg = 'JSONParsingError:'

    @property
    def files(self):
        return self.__files

    @property
    def ignoreFiles(self):
        return self.__ignoreFiles

    def __ReadFlag(self, value):
        if value in self.__trueSigns:
            return True
        if value in self.__falseSigns:
            return False
        raise JSONParsingError(f'Unknown value: {value}\nIt can be only {self.__trueSigns} or {self.__falseSigns}')

    def __ReadMod(self, mod, value):
        if mod == self.__ignorePrv:
            Set.ignorePrivate = self.__ReadFlag(value)
        elif mod == self.__ignorePrt:
            Set.ignoreProtected = self.__ReadFlag(value)
        elif mod == self.__ignorePrvCm:
            Set.ignorePrivateComps = self.__ReadFlag(value)
        elif mod == self.__ignorePrtCm:
            Set.ignoreProtectedComps = self.__ReadFlag(value)
        elif mod == self.__readOnlyDir:
            Set.readOnlyThisDirFiles = self.__ReadFlag(value)
        elif mod == self.__drawUndefCl:
            Set.drawUndefClasses = self.__ReadFlag(value)
        elif mod == self.__groupByFiles:
            Set.groupByFiles = self.__ReadFlag(value)
        elif mod == self.__drawOneClassGroup:
            Set.drawOneClassGroup = self.__ReadFlag(value)
        elif mod == self.__removeAccessPrefix:
            Set.removeAccessPrefix = self.__ReadFlag(value)
        elif mod == self.__altEngine:
            Set.altEngine = self.__ReadFlag(value)
        elif mod == self.__filesSign:
            self.__files = value
        elif mod == self.__ignoreFilesSign:
            self.__ignoreFiles = value
        elif mod == self.__colorSign:
            Set.classCol = value
        else:
            raise JSONParsingError(f'Unknown modification: {mod}')

    def Read(self):
        if not os.path.exists(self.__fileName):
            return

        try:
            with open(self.__fileName) as f:
                self.__settings = json.load(f)
        except json.decoder.JSONDecodeError as e:
            print(self.__readingErrorMsg, e)
        except Exception:
            print(self.__readingErrorMsg, 'Unexpected')

        for mod, value in self.__settings.items():
            try:
                if not type(mod) is str:
                    raise JSONParsingError(f'Modification must be string: {mod}')
                if type(value) is str:
                    self.__ReadMod(mod.lower(), value.lower())
                elif type(value) is list:
                    self.__ReadMod(mod.lower(), value)
                else:
                    raise JSONParsingError(f'Value must be string or list: {value}')
            except JSONParsingError as e:
                print(self.__parsingErrorMsg, e)
            except Exception:
                print(self.__parsingErrorMsg, 'Unexpected')
