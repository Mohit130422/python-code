#palindrome with fun
#palindrome number: is a number (in some base ) that is the same when written forwards or backwards, i.e., of the form. . The first few palindromic numbers are therefore are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121,
def palindrom(n):
    rev=0
    rem=0
    a=n
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if (a==rev):
        print(a,"is Palindrome")
    else:
        print(a,"is Not Palindrome")
def main():
    x=int(input("enter no"))
    palindrom(x)
if __name__== "__main__":
    main()
#run