

def getHeaderLumps():
    return 64

def getIntSize():
    return 4

def getIDSPHeader():
    return 1347633750

def getLMPOffset():
    return 20

def getLumpNames():  # from: https://developer.valvesoftware.com/wiki/Source_BSP_File_Format#Lump_types
    names = ["LUMP_ENTITIES", "LUMP_PLANES", "LUMP_TEXDATA", "LUMP_VERTEXES", "LUMP_VISIBILITY",
             "LUMP_NODES", "LUMP_TEXINFO", "LUMP_FACES", "LUMP_LIGHTING", "LUMP_OCCLUSION",
             "LUMP_LEAFS", "LUMP_FACEIDS", "LUMP_EDGES", "LUMP_SURFEDGES", "LUMP_MODELS"]
    return names