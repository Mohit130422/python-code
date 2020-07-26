#factorial with function
def factorial (n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def main():
    n=int(input("enter no."))
    res=factorial(n)
    print("result",res)
if __name__=="__main__":
    main()
#run
