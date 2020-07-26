#buddy pair with function
#buddy pairs
def buddy(n1,n2):
    i = 1
    j = 1
    sum1 = 0
    sum2 = 0
    while(i<=n1//2):
        if(n1%i==0):
            sum1=sum1+i
        i+=1
    while (j<=n2//2):
        if (n2%j==0):
            sum2=sum2+j
        j+=1
    if (n1==sum2 and n2==sum1):
        print(n1,"No. is Buddy Pairs with",n2)
    else:
        print(n1,"and",n2,"is not buddy pair.")
def main():
    x=int(input("enter no"))
    y=int(input("enter no"))
    buddy(x,y)
if __name__=="__main__":
    main()
    #run
# buddy pairs:-(220,284)(1184,1210)(2620, 2924)(5020, 5564)(6232, 6368)(10744, 10856)