#rock Paper Scissors
#import sys
def compare(a1,a2):
    if (a1==a2):
        return("It's a tie!")
    elif a1=='rock':
        if a2=='scissors':
            return(a1,"wins!")
        else:
            return(a2,"wins!")
    elif a1=='scissors':
        if a2=='paper':
            return(a1,"wins!")
        else:
            return(a2,"wins!")
    elif a1=='paper':
        if a2=='rock':
            return (a1,"wins!")
        else:
            return (a2,"wins!")
    else:
        return ("Invalid input! You have not entered rock, paper or scissors,try again.")
def main():
    a1 = input("what's your name?:")
    a2 = input("And your name?:")
    a1_answer = str(input("do you want to rock, paper or scissors?"))
    a2_answer = str(input("do you want to rock, paper or scissors?"))
    print(compare(a1_answer,a2_answer))
if __name__=="__main__":
    main()
#run




