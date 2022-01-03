import os

path = " # Enter the path here " 

if os.path.exists(path):
    print("The path is valid")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
    else:
        print("That is not a file")
else:
    print("File not exists")
