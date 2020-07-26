#palindrome range
print("Palindrome no range in 1 to 100")
for n in range(1,100):
    rev=0
    i=1
    a=n
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
        i+=1
    if(a==rev):
        print(a,"is Palindrome")
#run