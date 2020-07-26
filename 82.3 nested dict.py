#nested dict
d1={
    1:{"Name":"Mohit","Course":"Python","Fees":9000},
    2:{"Name":"Akhil","Course":"C sharp","Fees":8000},
    3:{"Name":"Ankit","Course":"Java","Fees":7000}
}
print(d1[1]['Course'])
print(d1[3]['Fees'])
print("---------------")
d1[3]['Fees']=10000
print(d1)
print("---------------")
del d1[3]['Fees']
print(d1)
print("---------------")
del d1[3]
print(d1)
#run