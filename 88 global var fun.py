#global Variable function.
b=12#global variable
def show():
    a=10#local variable
    a+=1
    print(a)
    print(b)
def main():
    show()
    print("--------------")
    print(b)
if __name__=="__main__":
    main()
    #run