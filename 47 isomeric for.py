#isomeric sum
print("Isomeric Numbers in 1 to 1000")
for n in range (1,1000):
    sum=0
    i=1
    while (i<=n//2):
        if (n%i==0):
            sum=sum+i
            #print(i, 'is factor of', n)
        i+=1
    if (n==sum):
        print("Isomeric No:",n)
#run

