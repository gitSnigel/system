# System
A base for a structure correction system

### Usage

To use default keywords
```sh
python splitCode.py
```

To use own keywords.txt
```sh
python splitCode.py keywords.txt
```

### What it does

It uses all files in src/ to look for structure.
It will create a directory structure/ for the output.
It will create a directory inside structure/ for each structure of the file that it finds and ofcourse add that file into the directory.

Because the structure easily gets to long to be a directory name I hashed the structure of the file as the directory name and
added a file called structure/*/structure.txt of the structure that has been found.
