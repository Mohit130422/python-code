d1={
    1:{"name":"Mohit","Course":"Python","Fees":6000},
    2:{"name":"Ankit","Course":"C++","Fees":4000},
    3:{"name":"Ansul","Course":"Flask","Fees":8000},
}
print(d1)
for k,v in d1.items():
    print("id:",k)
    for key in v:
        print(key,' ',v[key])
    print("--------------------")
    #run