def remove(sets):
#Discard() method will removes the element only when element present in sets if not
# it directly prints the sets without throwing any exception
    sets.discard(20)
# Remove() method will removes elem only when element present in sets if no element
# present in list it throws exception
    sets.remove(36)
    print(sets)
sets=set([10,20,26,41,20,21,36,40,45,36])

remove(sets)

