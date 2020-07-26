#value rverse
def main():
    n=int(input("enter no"))
    rev=0
    rem=0
    while (n>0):
        rem=n%10
        rev=rev*10+rem
        n = n//10
    print("Rverse=",rev)
if __name__=="__main__":
    main()
#run
