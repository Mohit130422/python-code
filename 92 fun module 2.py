#import module name as alias
import mymodule as bdm
def main():
    a=int(input("enter 1st no."))
    b=int(input("enter 2nd no."))
    r1=bdm.add(a,b)
    r2=bdm.sub(a,b)
    r3=bdm.mul(a,b)
    r4=bdm.div(a,b)

    print("add:-",r1,"sub:-",r2,"Mul:-",r3,"div:-",r4)
if __name__=="__main__":
    main()
    #run