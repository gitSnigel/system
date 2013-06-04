# coding=utf-8
import subprocess
import re
#mallen = open("Mall.java")
regexp = open("regexp.txt")

filnamn = "Fail.java"
filen = open(filnamn)
cmd = 'javac ' + filnamn 
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()

if err != None:
    print  "Dessa är dina compileringsfel: \n", err

loopar = 0
arrayList = 0
filestring = ''.join(filen.readlines(True))
print filestring
print [reg.strip() for reg in regexp]
print ''.join(regexp.readlines())
for reg in regexp:
    print re.findall(reg, filestring)
    if re.findall(reg, filestring) != -1:
        print reg + " finns"

for line in filen:
    if line.find('while') != -1 or line.find('for') != -1:
        loopar += 1
    elif line.find('ArrayList') != -1:
        arrayList +=1
           
print "\nAntal loopar: ", loopar 
print "\nAntal arraylist: " ,arrayList

