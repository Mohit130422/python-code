#function with default argument
def display(name="rahul",msg="good morning"):
    print("hello",name,msg)
def main():
    display(msg='xyz',name='abc')
if __name__=="__main__":
    main()
    #run