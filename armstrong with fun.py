#armstrong number:Armstrong number is a number that is equal to the sum of cubes 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
def armstrong(x):
    """this is my armstrong fun"""
    sum=0
    rem=0
    a=x
    while(x>0):
        rem=x%10
        sum=sum+(rem**3)
        x=x//10
    if (a==sum):
        print(a,"is armstrong no.")
    else:
        print(a,"is not armstrong no.")
def main():
    n=int(input("enter no."))
    b=armstrong(n)
if __name__=="__main__":
    main()
#run
