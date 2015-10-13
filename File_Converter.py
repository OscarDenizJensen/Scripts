import codecs
import os, sys

BLOCKSIZE = 1048576 # or some other, desired size in bytes

path=raw_input("Enter Path: ") #Get Path

dirs=os.listdir(path) #Get list of all the files in path

file_type=raw_input("Enter File Type") #File Type you want to search

change=raw_input("Change File Type to: ") #File Type you want to replace tp

files=open("files.txt","w") #Open a file to WRITE

##### Write Files with chosen file type to a text file
for file in dirs:
    if file_type==file[-len(file_type):]:
        files.write(file[:-len(file_type)]+"\n")


files=open("files.txt","r") #Open the file to READ

filesconvert = [line.rstrip('\n') for line in files]

print "Executing commands"

#Loop through commands
for i in (filesconvert):
    filein =path + i + file_type
    fileout =path + i + change
    #Change Coding Language with Codecs
    with codecs.open(filein, "r", "utf-8") as sourceFile:
        with codecs.open(fileout, "w", "ascii") as targetFile:
            while True:
                 contents = sourceFile.read(BLOCKSIZE)
                 if not contents:
                     break
                 targetFile.write(contents)

print("\n New Files Created")