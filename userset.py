import json
import os

from settings import *



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
        self.__filesSign = 'files'
        self.__ignoreFilesSign = 'ignorefiles'

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

    def __ReadMod(self, mod, value):
        if mod == self.__ignorePrv:
            Set.ignorePrivate = self.__ReadFlag(value)
        if mod == self.__ignorePrt:
            Set.ignoreProtected = self.__ReadFlag(value)
        if mod == self.__ignorePrvCm:
            Set.ignorePrivateComps = self.__ReadFlag(value)
        if mod == self.__ignorePrtCm:
            Set.ignoreProtectedComps = self.__ReadFlag(value)
        if mod == self.__readOnlyDir:
            Set.ReadOnlyThisDirFiles = self.__ReadFlag(value)
        if mod == self.__filesSign:
            self.__files = value
        if mod == self.__ignoreFilesSign:
            self.__ignoreFiles = value

    def Read(self):
        if not os.path.exists(self.__fileName):
            return

        with open(self.__fileName) as f:
            self.__settings = json.load(f)

        for mod, value in self.__settings.items():
            if value is str:
                self.__ReadMod(mod.lower(), value.lower())
            else:
                self.__ReadMod(mod.lower(), value)
