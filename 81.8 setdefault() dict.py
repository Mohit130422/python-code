#setdefault():- It is used to set default of a key.
d1={
    1:"mahi",
    2:"risk",
    3:"step"
}
res=d1.setdefault(1)
print(res)
print("---------------------------")
res1=d1.setdefault(4,"mohit")
print(res1)
print(d1)
print("---------------------------")
res2=d1.setdefault(5,"akhil")
print(res2)
print(d1)
#run