#from my module 2:- *
from mymodule import *
def main():
    a=int(input("enter first no."))
    b=int(input("enter second no."))
    r1=add(a,b)
    r2=sub(a,b)
    r3=mul(a,b)
    r4=div(a,b)
    print("add:-",r1,"sub:-",r2,"mul:-",r3,"div:-",r4)
if __name__=="__main__":
    main()
    #run