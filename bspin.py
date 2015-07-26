from bspinlib import fileIO, cli_parse, classes, constants
from bspinlib import lump_extract

commandline = cli_parse.parsecli()

bspobject = classes.BSPFile(commandline.filename)

file = open(bspobject.name,"rb")
bspobject.header = fileIO.readHeader(file)
file.close()

print(bspobject.header.toString(commandline.lump_info))

if commandline.extract_all:
    ids = list(map(str, range(constants.getHeaderLumps())))
    lump_extract.lump_load(bspobject, ids)
    for lid in ids:
        print("Extracting lump #%d ..." % (int(lid)))
        lump_extract.lump_extract(bspobject, lid)
        print("Done.")
    print("Done extracting all")
elif commandline.extract:
    print("Extracting lump #%d ..." % (int(commandline.extract)))
    lump_extract.lump_extract(bspobject, commandline.extract)
    print("Done.")