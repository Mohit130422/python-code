#prime no. in for loop
def main():
    n=int(input("enter no"))
    f=0
    for i in range(2,(n//2)+1):
        if (n%i==0):
            f=1
            break
    if(f==0):
        print("prime")
    else:
        print("Not prime")
if __name__=="__main__":
    main()
    #run