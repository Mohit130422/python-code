#evaluate factors
def main():
    i=1
    n=int(input("enter no:-"))
    while(i<=n//2):
        if(n%i==0):
            print(i,'is factor of',n)
            i+=1 #i=i+1
if __name__=="__main__":
    main()
    #run
