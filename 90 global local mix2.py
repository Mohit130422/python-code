#global & local variable function
a=12#global var
def show():
    global a
    a+=1
    print(a)
def main():
    show()
    print("-------------")
    print(a)
if __name__=="__main__":
    main()
    #run
    