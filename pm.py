def main():
    a=1
    b=101
    for i in range(a,b):
        f=0
        for j in range(2,(i//2)+1):
            if(i%j==0):
                f=1
                break
        if(f==0):
            print(i,' is prime')

if __name__=="__main__":
    main()