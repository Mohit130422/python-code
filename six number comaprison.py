#six no compare
a=int(input("enter first"))
b=int(input("enter second"))
c=int(input("enter third"))
d=int(input("enter forth"))
e=int(input("enter fifth"))
f=int(input("enter sixth"))
if (a >= b) and (a >= c) and (a >= d) and (a >= e) and (a >= f):
    maximum = a
    print (a,'is max')
elif (b >= a) and (b >= c) and (b >= d) and (b >= e) and (b >= f):
    maximum = b
    print(b,'is max')
elif (c >= a) and (c >= b) and (c >= d) and (c >= e) and (c >= f):
    maximum = c
    print(c,'is max')
elif (d >= a) and (d >= b) and (d >= c) and (d >= e) and (d >= f):
    maximum = d
    print(d,'is max')
elif (e >= a) and (e >= b) and (b >= c) and (e >= d) and (e >= f):
    maximum = e
    print(e,'is max')
else:
    maximum = f
    print(maximum,'is max')
    # run