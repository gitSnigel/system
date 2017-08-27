from os.path import join, isfile
import re
def splitCode(kod, keywords):#check structure of comments also?
    noDoubleComments="/*//*/".join(re.split("//.*\n",kod))#// comments
    noNewLines=noDoubleComments.replace("\n", " ") 
    noComments="/**/".join(re.split("/\*.*\*/", noNewLines))# /* */ comments
    escapedKeyWords=[re.escape(k) for k in keywords]#no escape?
    return re.split("(" + "|".join(escapedKeyWords) + ")", noComments)#split on space also?
def getStructure(codeList, keywords):
    code=[]
    structure=[]
    for p in codeList:
        w = p.strip()
        if w != "":
            code.append(w)
        if w in keywords:
            structure.append(w)
    return (code,structure)
    
def loadKeyWords(fileName):
    keywords=[]
    for l in open(fileName):
        keywords.append(l.strip())#what if regex want to be used
    return keywords

def copyStructure(keywords, f, dir, toDir):
    fil=open(join(dir, f)).read()
    codeList=splitCode(fil, keywords)
    structure=getStructure(codeList, keywords)[1]
    copyFile.copyFile(f, dir,toDir," ".join(structure))
    
if __name__ == "__main__":
    import os,sys
    import copyFile
    dir="src/"
    toDir="structure/"
    keywords = ["(", ")", "{", "}", "[","]", ".", "=", ";"]
    if len(sys.argv) > 1:#keywords file
        keywords=loadKeyWords(sys.argv[1])
        #print "keywords:", keywords
        if len(sys.argv) > 2:#from dir
            dir=sys.argv[2]
            if len(sys.argv) > 3:#to dir
                toDir=sys.argv[3]
    files=os.listdir(dir)
    for f in files:
        fil=join(dir, f)
        if not isfile(fil):#no directories
            continue
        copyStructure(keywords, f, dir, toDir)
    #if not os.path.exists("hashes"):
    #    os.makedirs("hashes")
    #copyFile.writeAllHashes("hashes")
