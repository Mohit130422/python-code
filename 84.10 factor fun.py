#no. of factor function.
def fact(x):
    if (x==1):
        return 1
    else:
        return x*fact(x-1)
def main():
    n=int(input("Enter no."))
    res=fact(n)
    print("res=",res)
if __name__=="__main__":
    main()
    #run
