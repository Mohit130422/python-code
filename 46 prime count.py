#prime no count
a =int(input("enter no.:"))
count=0
for n in range (1,1000):
    f=0
    for i in range(2,(n//2)+1):
        if (n%i==0):
            f=1
            break
    if (f==0):
        count+=1
        #print(n)
        if(a==count):
            print(n,"is",a,"th prime no")
    #run


