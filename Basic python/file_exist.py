#To check wheather a file exist or not in a directory
import os.path
if os.path.isfile("abc.txt"):
    print("file exist")
else:
    print("File doesn't exist")