#count factors
def main():
    i=1
    count=0
    n=int(input("enter Number:-"))
    while(i<=n//2):
        if(n%i==0):
            count=count+1
            print(i,'is factor of',n)
        i+=1

    print('count=',count)
if __name__=="__main__":
    main()
    #run
