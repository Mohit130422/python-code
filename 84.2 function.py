#types of Function
#Function without argument and written type.

def add():
    """this is my add fun"""
    a=int(input("Enter first no."))
    b=int(input("Enter Second no."))
    c=a+b
    #print("sum=".str+(c))
    print("sum=",c)
def main():
    add()
    print(add.__doc__)
if __name__=="__main__":
    main()
#run