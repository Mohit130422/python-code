#copy() returns a shallow copy of a dictionary
d1={
    1:"abc",
    2:"jkl",
    3:"cde"
}
d2=d1
print(d1,'d1 dict')
print(d2,'d2 dict')
print("--------after update-----------")
d2[1]="aaa"
print(d1,'d1 dict')
print(d2,'d2 dict')
print("-----------------")
d3=d1.copy()
print(d3,'d3 dict')
d3[1]="bcb"
print(d1,'d1 dict')
print(d3,'d3 dict')
#run