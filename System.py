# coding=utf-8
import subprocess

#    mallen = open("Mall.java")
filen = open("Fail.java")
cmd = 'javac ' + 'Fail.java' 
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()

if err != None:
    print  "Dessa är dina compileringsfel: \n", err

loopar = 0
arrayList = 0

for line in filen:
    if line.find('while') != -1 or line.find('for') != -1:
        loopar += 1
    elif line.find('ArrayList') != -1:
        arrayList +=1
           
print "\nAntal loopar: ", loopar 
print "\nAntal arraylist: " ,arrayList

