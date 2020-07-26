#four no compare
a=int(input("enter first"))
b=int(input("enter second"))
c=int(input("enter third"))
d=int(input("enter forth"))
if(a>b):
    if(a>c):
        if(a>d):
            print(a,"is max")
        else:
            print(d,"is max")
    else:
        if(c>d):
            print(c,'is max')
        else:
            print(d,'is max')
else:
    if(b>c):
        if(b>d):
            print(b,'is max')
        else:
            print(d,'is max')
    else:
        if(c>d):
            print(c,'is max')
        else:
            print(d,'is max')
            # run