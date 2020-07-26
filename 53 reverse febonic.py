#reverse febonica series
a=0
b=1
n= int(input("enter terms"))
print(a,' ',b,end=' ')
for i in range(1,n-1):
    c=b-a
    print(c,end=' ')
    b=a
    a=c
#run