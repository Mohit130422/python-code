#global & local variable.
b=12#global var
def show():
    a=10#local var
    global b
    a+=1
    b+=1
    print(a)
    print(b)
def main():
    show()
    print("------------")
    print(b)
if __name__=="__main__":
    main()
    #run

