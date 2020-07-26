#sum of factors
def main():
    i=1
    sum=0
    n=int(input("enter no"))
    while (i<=n//2):
        if(n%i==0):
            sum=sum+i
            print(i,'is factor of',n)
        i+=1
    if(n==sum):
        print("Isomeric Number")
    else:
        print("Not Isomeric")
if __name__=="__main__":
    main()
#run