def frst_char(list_word):
    char=list_word.split(" ")
    for word in char:
        print(word[0],end="  ")
list_word="Hi! welcome to bridgelabz"
frst_char(list_word)