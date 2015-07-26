from bspinlib import constants, misc


class BSPFile:
    def __init__(self, name):
        self.header = None
        self.name = name
        self.lump_data = {}  # loaded only if needed


class BSPHeader:
    def __init__(self):
        self.ident = 0
        self.version = 0
        self.lumps = []
        self.mapRevision = 0

    def insertLump_t(self, lumpt):
        self.lumps.append(lumpt)
        if len(self.lumps) > constants.getHeaderLumps():
            return False
        return True

    def isValid(self):
        return self.ident == constants.getIDSPHeader()

    def toString(self, printLumps=False):
        ret = ""
        ret += "BSP Header:\n"
        if self.isValid():
            valid = "valid"
        else:
            valid = "invalid"
        ret += "%s Ident: %d (%s)\n" % (misc.indent(1), self.ident, valid)
        ret += "%s Version: %d\n" % (misc.indent(1), self.version)
        ret += "%s Map Revision: %d\n" % (misc.indent(1), self.mapRevision)
        if printLumps:
            for i in range(constants.getHeaderLumps()):
                ret += self.lumps[i].toString()
        return ret

class Lump_t:
    def __init__(self):
        self.lumpID = 0
        self.fileofs = 0
        self.filelen = 0
        self.version = 0
        self.fourCC = []

    def toString(self):
        ret = ""
        ret += "%s Lump #%d (%s):\n" % (misc.indent(1), self.lumpID, "to be implemented")
        ret += "%s File offset (byte): %d\n" % (misc.indent(2), self.fileofs)
        ret += "%s Length (bytes): %d\n" % (misc.indent(2), self.filelen)
        ret += "%s Version: %d\n" % (misc.indent(2), self.version)
        ret += "%s FourCC: " % (misc.indent(2),)
        for i in range(4):
            ret += "%d " % (self.fourCC[i],)
        if self.lumpID < constants.getHeaderLumps()-1:
            ret += "\n"
        return ret