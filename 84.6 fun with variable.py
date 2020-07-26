#function with variable:-
def display(*x):
    """this is my variable fun"""
    print(x)
    print("----")
    for i in x:
        print(i)
def main():
    mylist=[1,2,3,4,5,6]
    display(mylist)
    display(10)
    display(1,2,3)
    print(display.__doc__)
if __name__=="__main__":
    main()
#run

