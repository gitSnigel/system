# coding=utf-8
import subprocess
import re
mallen = open("Mall.java").readlines()
regexp = open("regexp.txt").readlines()

filnamn = "Fail.java"
filen = open(filnamn).readlines()

cmd = 'javac ' + filnamn

proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()

if err != None:
    print  "Dessa är dina compileringsfel: \n", err

#kollar mall mot regexp
mall = []
mallstring = ''.join(mallen)
for i, reg in enumerate(regexp):
    exists = re.findall(reg.strip(), mallstring)
    mall.append(len(exists))

#kollar inl mot regexp och mallens regexp
filestring = ''.join(filen)
for i, reg in enumerate(regexp):
    exists = re.findall(reg.strip(), filestring)
    if exists:
        print reg.strip() + " finns "+ str(len(exists)) + " st"
    if mall[i] != len(exists):
        print reg.strip() + " skiljer sig från mallen"
    



loopar = 0
arrayList = 0

for line in filen:
    if line.find('while') != -1 or line.find('for') != -1:
        loopar += 1
    elif line.find('ArrayList') != -1:
        arrayList +=1
           
print "\nAntal loopar: ", loopar 
print "\nAntal arraylist: " ,arrayList

