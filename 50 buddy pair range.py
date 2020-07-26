#Buddy Pair range....
for n1 in range(1,10000):
    s1=0
    s2=0
    i=1
    j=1
    while(i<=n1//2):
        if(n1%i==0):
            s1=s1+i
        i+=1
    n2=s1
    while(j<=n2//2):
        if(n2%j==0):
            s2=s2+j
        j+=1
    if(n1==s2 and n2==s1):
        print(n1,' ',n2,' are buddy pair')
    #run


