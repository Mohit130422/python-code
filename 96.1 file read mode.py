#step 1- create a python file with any name.
#step 2- create a data in that python file.
#step 3- open another .py file and write a programme.
#eg.
def main():
    f=open("filehandling.py","r")
    print(type(f))
    data=f.read()
    #data=f.read(200)use if you want to restriction in your life.
    print(data)
    f.close()
if __name__=="__main__":
    main()