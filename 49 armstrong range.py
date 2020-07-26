#armstrong numbers range
print("Armstron btween 1 to 1000:")
for n in range (1,1000):
    rem=0
    i=1
    sum=0
    a=n
    while(n>0):
        rem=n%10
        sum=sum+(rem**3)
        n=n//10
    i+=1
    if (a==sum):
        print("Armstrong:",a)
    #run
