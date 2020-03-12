class removeElements:
    def specific_List(self,List):
        print("Removeing List : ",List[1],List[2],List[3])
    def delToPrint(self,List):
        del (List[0],List[4],List[3])
        print("Del Function : ",List)
List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
specifiedVal=removeElements()
specifiedVal.specific_List(List)
specifiedVal.delToPrint(List)