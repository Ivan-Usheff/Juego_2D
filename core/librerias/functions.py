import os,sys,importlib


def relativeImportPath(myfile):
    pathname, filename = os.path.split(myfile)
    sys.path.append(os.path.abspath(pathname))
    modname = os.path.splitext(filename)[0]
    mymod = importlib.import_module(modname)
    return mymod