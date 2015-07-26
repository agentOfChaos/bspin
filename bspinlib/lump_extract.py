import os
import struct
from bspinlib import fileIO, constants

def lump_load(bspobject, id_list):
    in_fname = bspobject.name
    inputfile = open(in_fname, "rb")
    for lid in id_list:
        fileIO.loadLumpData(inputfile, bspobject, lid)
    inputfile.close()

def lump_extract(bspobject, lid):
    out_fname = os.path.splitext(bspobject.name)[0] + "_l_" + lid + ".lmp"

    if lid not in bspobject.lump_data:
        lump_load(bspobject,[lid])

    outfile = open(out_fname, "wb")

    outfile.write(struct.pack("i", constants.getLMPOffset()))
    outfile.write(struct.pack("i", int(lid)))
    outfile.write(struct.pack("i", bspobject.header.lumps[int(lid)].version))
    outfile.write(struct.pack("i", bspobject.header.lumps[int(lid)].filelen))
    outfile.write(struct.pack("i", bspobject.header.mapRevision))
    outfile.write(bspobject.lump_data[lid])

    outfile.close()