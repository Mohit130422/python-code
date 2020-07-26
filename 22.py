#mini calculator
def calc (x,y,n):
    d1={
        1:x+y,
        2:x-y,
        3:x*y,
        4:x//y,
    }
    return d1.get(n,"please enter only:-1to4")
def main():
    print("1:Add\n2:Sub\n3:Multiply\n4:Division")
    choice=int(input("enter your choice"))
    a=int(input("First no"))
    b=int(input("second no"))
    res=calc(a,b,choice)
    print("res=",res)
if __name__=="__main__":
    main()