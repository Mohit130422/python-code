#calculate palindrom no.
n= int(input("enter no"))
n1=n//100
n2=n%100
n11=n1//10
n12=n1%10
n21=n2//10
n22=n2%10
if(n11==n22 and n12==n21):
    print("It is Palindrome")
else:
    print("It is not Palindrome")
#run
