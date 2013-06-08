# coding=utf-8
import subprocess
import re

def compileFile(filename):#om alla klasser ska vara lika så måste alla filnamn vara lika också.
    cmd = 'javac ' + filename
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err != None:
        print "\nDessa är dina kompileringsfel: \n", err
    else:
        print "\nDu hade inga kompileringsfel! \n"

mall = []
def addToMall(exists,reg,i):
    size = len(exists)
    if not size:
        print "Varning: " + reg + " finns inte i mallen"
    mall.append(size)

def existsInFile(exists,reg,i):
    if exists:
        print reg + " finns", len(exists), "st"
    if mall[i] != len(exists):
        print reg + " skiljer sig från mallen"

def readFileIntoList(filename):
    return [line.strip() for line in open(filename).readlines()]

regexp = readFileIntoList("regexp.txt")
def checkAgainstRegexp(filename, method):
    filestring = ''.join(readFileIntoList(filename))
    for i, reg in enumerate(regexp):
        exists = re.findall(reg.decode("string_escape"), filestring)#kompilerings fel i regexpet
        method(exists,reg,i)

if __name__ == "__main__":
    import sys
    mallen = "Mall.java"
    files = ["Fail.java"]
    if len(sys.argv) > 2:
        mallen = sys.argv[1]
        files = sys.argv[2:]
    elif len(sys.argv) == 2:
        mallen = sys.argv[1]
        from os import listdir
        from os.path import isfile, join
        files = [ f for f in listdir(".") if isfile(f) and f.endswith(".java") ]
        # TODO vilka filer ska vara med?

    #kollar mall mot regexp
    checkAgainstRegexp(mallen, addToMall)
    
    for filename in files:
        compileFile(filename)
        #kollar inl mot regexp och mallens regexp
        checkAgainstRegexp(filename, existsInFile)


