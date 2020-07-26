#sum of factors
def fact(n):
    '''this is my isomeric function...'''
    i=1
    sum=0
    while(i<=n//2):
        if(n%i==0):
            sum=sum+i
            print(i,'is factor of',n)
        i+=1
    if (n==sum):
        print(n,"is isomeric no.")
    else:
        print(n,"is not isomeric no.")
def main():
    x=int(input("enter no:"))
    fact(x)
    print(fact.__doc__)
if __name__=="__main__":
    main()
#run