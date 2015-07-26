import struct
from bspinlib import classes, constants

intsize = constants.getIntSize()
headerLumps = constants.getHeaderLumps()

#  references:  https://developer.valvesoftware.com/wiki/Source_BSP_File_Format
#               https://developer.valvesoftware.com/wiki/Lump_file_format

def readHeader(binfile):
    header = classes.BSPHeader()
    header.ident = struct.unpack("i", binfile.read(intsize))[0]
    header.version = struct.unpack("i", binfile.read(intsize))[0]
    for i in range(headerLumps):
        newlump = readLump_t(binfile)
        newlump.lumpID = i
        header.lumps.append(newlump)
    header.mapRevision = struct.unpack("i", binfile.read(intsize))[0]
    return header

def readLump_t(binfile):
    lumpt = classes.Lump_t()
    lumpt.fileofs = struct.unpack("i", binfile.read(intsize))[0]
    lumpt.filelen = struct.unpack("i", binfile.read(intsize))[0]
    lumpt.version = struct.unpack("i", binfile.read(intsize))[0]
    lumpt.fourCC.extend(struct.unpack("BBBB", binfile.read(4)))
    return lumpt

def loadLumpData(binfile, bspobject, id):
    lump_t = bspobject.header.lumps[int(id)]
    offset = lump_t.fileofs
    length = lump_t.filelen
    bspobject.lump_data[id] = readRawBytes(binfile, offset, length)

def readRawBytes(binfile, offset, length):
    binfile.seek(offset, 0)
    return binfile.read(length)