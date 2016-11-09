import os, hashlib
from os.path import join, exists
from shutil import copyfile

spSign="+"

def repl(name, before, after):
    return name.replace(before,spSign*3+after+spSign*3)

def fixFileName(name):#TODO better filenames
    backslash=repl(name, "\\", "backslash")
    slash=repl(backslash, "/", "slash")
    colon=repl(slash, ":", "colon")
    star=repl(colon, "*", "star")
    pipe=repl(right, "|", "pipe")
    left=repl(pipe, "<", "left")
    right=repl(left, ">", "right")
    return repl(star, "?", "quesionmark")

def writeDir(path, directory, struct):
    fullDir=join(path, fixFileName(directory))
    if not exists(fullDir):
        os.makedirs(fullDir)
        f = open(fullDir + "/struct.txt", 'w')
        f.write(struct)
        f.close()

def copyFile(fileName, fromPath, toDir, structureDir):
    hash = getHashOfString(structureDir)
    writeDir(toDir, hash, structureDir)
    copyfile(join(fromPath,fileName), join(toDir, hash, fileName))

structmap=dict()
def getHashOfString(string):
    hash = hashlib.md5(string).hexdigest()
    saveHash(hash, string)
    return hash

def saveHash(key, value):
    structmap[key]=value

def writeAllHashes(map):
    for k,v in structmap.items():
        f = open(join(map,k),'w')
        f.write(v+'\n') 
        f.close()
