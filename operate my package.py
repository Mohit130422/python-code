#package executer
import bodmass
def main():
    a=float(input("enter First No"))
    b=float(input("enter second no"))

    r1=bodmass.add(a,b)
    r2=bodmass.sub(a,b)
    r3=bodmass.mul(a,b)
    r4=bodmass.div(a,b)
    print(r1,' ',r2,' ',r3,' ',r4)
if __name__=="__main__":
    main()

