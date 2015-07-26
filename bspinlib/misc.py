
indentstr = "   "

def indent(level):
    ret = ""
    for x in  range(level):
        ret += indentstr
    return ret