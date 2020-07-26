#function:- is a "Re-usable" block of code.
#example:-

def show():
    """this is my fun"""
    print("Hello world")
def main():
    show()
    print(show.__doc__)
if __name__=="__main__":
    main()
#run