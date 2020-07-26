#power with function

def power(x,y):
    """this is my power fun"""
    f=1
    for i in range(1,y+1):
        f=f*x
    return f
def main():
    n=int(input("enter no."))
    p=int(input("enter Power:"))
    res=power(n,p)
    print("result:-",res)
    print(power.__doc__)
if __name__=="__main__":
    main()
#run
