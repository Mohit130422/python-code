#write mode file handling:-
def main():
    f=open("filehandling.py","w")
    f.write("I Love You 3000")
    f.write("\n")
    f.write("some infinities are bigger than other infinities.")
    print("successfully written.........")
    f.close()
if __name__ == '__main__':
    main()
    #run