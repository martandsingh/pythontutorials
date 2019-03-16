'''
    Author : Martand Singh
    Date: 16 Mar 2019
    Scope : file handling in python
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
   
'''
import os # for file rename and directory handling

# Provides the basic info about given file
def getFileDetail(filename):
    fp = open(filename, "r")
    print("> Filename: ", fp.name)
    print("> File access mode: ", fp.mode)
    print("> Is file closed: ", fp.closed)
    fp.close()
    print("> Is file closed: ", fp.closed)

# Returns the content of the file as string
def getFileContent(filename):
    fp = open(filename, "r")
    content = fp.read()
    fp.close()
    return content

# Writes a file in text mode
def writeTextFile(filename):
    fp = open(filename, 'w')
    fp.write('''
    Hello this is the python test file.
    We are writing a file using python file handling utility.
    It is really cool...!!! yAAy
    ''')
    fp.close()
    print("> file create successfully.")

# Rename a file
def renamefile(oldname, newname):
    os.rename(oldname, newname)
    print("> File renamed.")

# Make directory
def createDirectory(directoryName):
    os.mkdir(directoryName)
    print("> Directory created.")

# Delete file
def deleteFile(filename):
    os.remove(filename)
    print("> File deleted successfully.")



# Print detail of the file
getFileDetail("datetime.py")
# Reading a file
content = getFileContent("datetime.py")
print("> Content of datetime.py file: ")
print(content)
# Writing a file
writeTextFile("test.txt")
# Renaming file
renamefile("test.txt", "renamedtest.txt")
# Make directory
createDirectory("test dir")
createDirectory("test dir2")
# Remove dir
os.rmdir("test dir2")