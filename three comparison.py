#three digit comparison
a= int(input("enter first no"))
b= int(input("enter second no"))
c= int(input("enter third no"))
if(a>b):
    if(a>c):
        print(a,'is maximum')
    else:
        print(c,'is maximum')
else:
    if(b>c):
        print(b,'is maximum')
    else:
        print(c,'is maximum')
#run
