#prime no in two numbers range
def main():
    n1=int(input("enter first no:"))
    n2=int(input("enter second no:"))
    for i in range(n1,n2+1):
        f=0
        for j in range(2,(i//2)+1):
            if(i%j ==0):
                f=1
                break
        if(f==0):
            print("Prime No.",i)
if __name__=="__main__":
    main()

#run

