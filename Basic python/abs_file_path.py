#Program to find the absolute file path
import os
def abs_file_path(path_name):
    return os.path.abspath("path_name")
print("Absolute file path: ",abs_file_path("test.txt"))
