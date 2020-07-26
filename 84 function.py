#function with argument with data type
def add(x,y):
    '''this is my add function'''
    c=x+y
    return c
def main():
    a=int(input("enter 1st no."))
    b=int(input("enter 2nd no."))
    r=add(a,b)
    print("sum=",r)
    print(add.__doc__)
if __name__ == '__main__':
    main()
#run