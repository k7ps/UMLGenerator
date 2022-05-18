from settings import *

#@UML clusters Parsing
class ModificationChecker:
    umlSign = Set.pyUmlSign 
    aggrSign = Set.aggrSign
    clustSign = Set.clustSign
    ignoreSign = Set.ignoreSign
    
    def ReadLine(line):
        mods = {}
        start = line.find(ModificationChecker.umlSign)
        if start == -1:
            return mods
        line = line[start+len(ModificationChecker.umlSign):]
        signs = line.split(sep=';')
        for i in range(len(signs)):
            mods.update (ModificationChecker.ReadSign(signs[i]))
        return mods
        
    def ReadSign(signStr):
        sign = signStr.split()
        sign[0] = sign[0].lower()
        if ModificationChecker.aggrSign.startswith (sign[0]):
            return {ModificationChecker.aggrSign: True}
        if ModificationChecker.ignoreSign == sign[0]:
            return {ModificationChecker.ignoreSign: True}
        if ModificationChecker.clustSign == sign[0]:
            clustStr = ''.join(sign[1:])
            clusters = clustStr.split(sep=',')
            return {ModificationChecker.clustSign: clusters}
        return {}

    def GetClusters(mods):
        clusters = []
        if ModificationChecker.clustSign in mods:
            clusters = mods[ModificationChecker.clustSign]
        return clusters

    def GetIgnore(mods):
        if ModificationChecker.ignoreSign in mods:
            return mods[ModificationChecker.ignoreSign]
        return False

    def GetAggr(mods):
        if ModificationChecker.aggrSign in mods:
            return mods[ModificationChecker.aggrSign]
        return False

    def ReadClass(line):
        mods = ModificationChecker.ReadLine(line)
        clusters = ModificationChecker.GetClusters(mods)
        ignore = ModificationChecker.GetIgnore(mods)
        return clusters, ignore

    def ReadMethod(line):
        mods = ModificationChecker.ReadLine(line)
        ignore = ModificationChecker.GetIgnore(mods)
        return ignore

    def ReadVariable(line):  
        mods = ModificationChecker.ReadLine(line)
        aggr = ModificationChecker.GetAggr(mods)
        ignore = ModificationChecker.GetIgnore(mods)
        return aggr, ignore
