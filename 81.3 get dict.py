#get() obtain a element on the key.
d1={
    1:"Mohit",
    2:"Rohit",
    3:"Ranu"
}
res=d1.get(1)
print(res)
res1=d1.get(12)
print(res1)
res2=d1.get (12,"key not found")
print(res2)
#print(d1[12}) error
#run
#in case of got method if key is not found it returns none where as in case of this
# approach it shows key error.

