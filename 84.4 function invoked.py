#How Function invoked:-
def show():
    print("shadow invoked")
def main():
    print("main invoked")
    show()
    print("Control back to main")
if __name__=="__main__":
    main()
#run