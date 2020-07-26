#Global&local variable:- A variable which is declared outside any function is known as global variable. where is a variable in sight a function is known as local variable."
def show():
    a=10#local variable
    print(a)
def main():
    show()
    print(a)
if __name__=="__main__":
    main()
#run
#error:- NameError: name 'a' is not defined.Because 'a' is local variable NOT Global.


