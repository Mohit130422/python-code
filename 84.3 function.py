#function with argument and no return type
def add(x,y):
    """this is my another add fun"""
    c=x+y
    print("sum=",c)
def main():
    a=int(input("enter first no."))
    b=int(input("enter second no."))
    add(a,b)#print(a+b)
    print(add.__doc__)
if __name__=="__main__":
    main()
#run

