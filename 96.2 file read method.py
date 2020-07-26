#file reading Method:-
def main():
    f=open("filehandling.py","r")
    print(type(f))
    data1=f.readline()
    data2=f.readline()
    data3=f.readline()
    data4=f.readline(10)
    print(data1,end='')
    print(data2,end='')
    print(data3,end='')
    print(data4,end='')
    f.close()
if __name__ == '__main__':
    main()
    #run