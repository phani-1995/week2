import os.path,time
print("last modified: %s" % time.ctime(os.path.getmtime("test.txt")))

print("created: %s" % time.ctime(os.path.getctime("test.txt")))