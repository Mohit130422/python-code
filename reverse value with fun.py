#value rverse with function
def reverse(x):
    """this is my reverse function"""
    rev=0
    rem=0
    while(x>0):
        rem=x%10
        rev=rev*10+rem
        x=x//10
    print("Reverse Value is:-",rev)
def main():
    n=int(input("enter no.:"))
    reverse(n)
    print(reverse.__doc__)
if __name__=="__main__":
    main()
#run
