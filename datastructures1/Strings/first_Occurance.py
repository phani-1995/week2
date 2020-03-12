class change_frst_rep:
    def frst_rep(self,string):
        for i in string:
            if (i=='r'):
                i='$'
            print(i,end='')
    def change_char(self,str1):
        char=str1[0]
        str1=str1.replace(char,'$')
        str1=char+str1[1:]
        print(str1)
string='restart'
chng_str=change_frst_rep()
chng_str.frst_rep(string)
chng_str.change_char(string)