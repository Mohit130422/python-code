#function with default argument
def display (name="rahul",msg="good morning"):
    print("hello",name,msg)
def main():
    display("akhil","good evening")
    display("mohit")
    display()
if __name__=="__main__":
    main()
    #run

"""def display(name="xarvis",msg):
    print("Hello",name,':',msg)
    #SyntaxError: non-default argument follows default argument"""