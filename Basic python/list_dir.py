#  Write a Python program to list all files in a directory in Python
from os import listdir
from os.path import isfile, join
class listFileDir:
    def filesDir(self):
        files_list = [f for f in listdir('/home/bridgelabz/Desktop/week2/Basic python')
                      if isfile(join('/home/bridgelabz/Desktop/week2/Basic python', f))]
        print(files_list)
listfile=listFileDir()
listfile.filesDir()
