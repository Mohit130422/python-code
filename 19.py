#nested if/else- calculate leap year
year= int(input("enter no"))
if(year%400==0):
    print("leap year")
else:
    if(year%4==0):
        if(year%100!=0):
            print("leap year")
        else:
            print("No leap year")
    else:
        print("Not")
#run
