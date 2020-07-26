#buddy pairs
def main():
    i=1
    j=1
    sum1=0
    sum2=0
    n1=int(input("enter no"))
    n2=int(input("enter no"))
    while(i<=n1//2):
        if (n1%i == 0):
            sum1=sum1+i
        i+=1

    while(j<=n2//2):
        if (n2%j==0):
            sum2=sum2+j
        j+=1
    if(n1==sum2 and n2==sum1):
        print("No. is Buddy Pairs")
    else:
        print("No. is not")
if __name__=="__main__":
    main()
    #run
# buddy pairs:-(220,284)(1184,1210)(2620, 2924)(5020, 5564)(6232, 6368)(10744, 10856)