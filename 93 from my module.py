#from my module (add(),sub(),mul(),div())
from bodmass import add,sub,mul,div
def main():
    a=int(input("enter 1st no."))
    b=int(input("enter 2nd no."))
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
    print(div(a,b))
if __name__=="__main__":
    main()
