from bspinlib import fileIO, cli_parse, classes
from bspinlib import lump_extract

commandline = cli_parse.parsecli()

bspobject = classes.BSPFile(commandline.filename)

file = open(bspobject.name,"rb")
bspobject.header = fileIO.readHeader(file)
file.close()

print(bspobject.header.toString(commandline.lump_info))

if commandline.extract:
    print("Extracting lump #%d" % (int(commandline.extract)))
    lump_extract.lump_extract(bspobject, commandline.extract)