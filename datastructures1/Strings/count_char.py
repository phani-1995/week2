class char_count:
    def count_char(self,string):
        for i in range(len(string)-1):
            count=0
            for j in range(len(string)-1):
                if string[i] == string[j]:
                    count+=1
            print(string[i],":",count,end=" ")
    def char_freq(self,string1):
        dict={}
        for k in string1:
            keys=dict.keys()
            if k in keys:
                dict[k] += 1
            else:
                dict[k] = 1
        return dict
string = 'World Wide Web'
lenstr=char_count()
lenstr.count_char(string)
print(lenstr.char_freq(string))