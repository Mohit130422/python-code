#table by while loop (2x1=2)
def main():
    i=1
    n=int(input("enter no"))
    while(i<=10):
        r=n*i
        print(n,'*',i,'=',r)
        i+=1
if __name__=="__main__":
    main()
