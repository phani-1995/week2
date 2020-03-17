import os
def list_IDs():
    print("Effective group Id : ",os.getegid())
    print("Effective user Id : ",os.geteuid())
    print("Real group Id : ",os.getgid())
    print("Supplimentary group Ids: ", os.getgroups())
list_IDs()