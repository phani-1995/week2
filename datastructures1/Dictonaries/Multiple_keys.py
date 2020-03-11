def check_key(data):
    print(data.keys()>={'class','Name'})
    print(data.keys()>={'India','Run'})
    print(data.keys()>={'color','name'})
data={"Name":"India", "color":"Orange","class":"XI"}
check_key(data)