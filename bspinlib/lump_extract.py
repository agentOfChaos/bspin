import os
import struct
from bspinlib import fileIO, constants

def lump_extract(bspobject, id):
    out_fname = os.path.splitext(bspobject.name)[0] + "_l_" + id + ".lmp"

    if id not in bspobject.lump_data:
        in_fname = bspobject.name
        inputfile = open(in_fname, "rb")
        fileIO.loadLumpData(inputfile, bspobject, id)
        inputfile.close()

    outfile = open(out_fname, "wb")

    outfile.write(struct.pack("i", constants.getLMPOffset()))
    outfile.write(struct.pack("i", int(id)))
    outfile.write(struct.pack("i", bspobject.header.lumps[int(id)].version))
    outfile.write(struct.pack("i", bspobject.header.lumps[int(id)].filelen))
    outfile.write(struct.pack("i", bspobject.header.mapRevision))
    outfile.write(bspobject.lump_data[id])

    outfile.close()