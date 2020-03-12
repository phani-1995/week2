class add_ing_ly:
    def add_ing(self,string):
        if (len(string)==3):
            string=string+'ing'
            print(string)
    def add_ly(self,str1):
        if (str1[-3]=='ing'):
            str1=str1+'ly'
            print(str1)
string='abc'
str1='string'
adding=add_ing_ly()
adding.add_ing(string)
adding.add_ly(str1)


