#power of number.
def power(x,y):
    f=1
    if (y==0):
        return 1
    elif(y==1):
        return x
    else:
        f=(x*power(x,y-1))
        return f
def main():
    n=int(input("enter no."))
    p=int(input("enter power"))
    res=power(n,p)
    print("res=",res)
if __name__=="__main__":
    main()
#run