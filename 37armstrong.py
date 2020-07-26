#armstrong number:Armstrong number is a number that is equal to the sum of cubes 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
def main():
    n=int(input("enter no"))
    sum=0
    rem=0
    a=n
    while(n>0):
        rem=n%10
        sum=sum+(rem**3)
        n=n//10
    if(a==sum):
        print("Armstrong")
    else:
        print("Not")
if __name__=="__main__":
    main()
#run
