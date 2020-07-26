#nested dict
d1={
    1:{"Name":"Mohit","Course":"Python","Fees":9000},
    2:{"Name":"Akhil","Course":"C sharp","Fees":8000},
    3:{"Name":"Ankit","Course":"Java","Fees":7000}
}
d1[4]={}
d1[4]['name']='rahul'
d1[4]['Course']='HTML'
d1[4]['Fees']='6000'
print(d1)
#run