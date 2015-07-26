import argparse

def parsecli():
    parser = argparse.ArgumentParser(description="Utility tool for mainpulating .bsp files (map files used"
                                                 " in Valve's Source Engine)")
    parser.add_argument('--lump-info', '-l', help='Print lump informations', action='store_true')
    parser.add_argument('--extract', '-X', metavar='id', help='Extract a specific lump to a .lmp file')
    parser.add_argument('filename', metavar='filename', help='bsp file to load', type=str)
    return parser.parse_args()