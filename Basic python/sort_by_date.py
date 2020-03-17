import glob
import os
file=glob.glob("*.txt")
file.sort(key=os.path.getmtime)
print("\n".join(file))
