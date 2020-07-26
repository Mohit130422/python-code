# A Module is simply a python file which containing function or Data.
# a. import module name
# b. import module name import fun/data
# c. import module name import*
import mymodule
def main():
    a=int(input("Enter First no."))
    b=int(input("Enter Second no."))
    r1=mymodule.add(a,b)
    r2=mymodule.sub(a,b)
    r3=mymodule.mul(a,b)
    r4=mymodule.div(a,b)
    print("add:-",r1,"sub:-",r2,"Mul:-",r3,"division:-",r4)
if __name__=="__main__":
    main()
    #run