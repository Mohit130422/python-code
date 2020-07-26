#week days with switch case
def show(n):
    d1={
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thrusday",
        6:"Friday",
        7:"Saturday",
    }
    return d1.get(n)
def main():
    day=int(input("enter no"))
    res=show(day)
    print("Day is",res)
if __name__=="__main__":
    main()
#run
