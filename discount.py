#dicount & payment
amnt=int(input("enter amount"))
payment=0
disc=0
if(amnt>5000):
    disc=amnt*(0.10)
    print("disc",disc)
    payment=(amnt-disc)
    print("payment",payment)
else:
    disc=amnt*(0.02)
    print("disc",disc)
    payment=(amnt-disc)
    print("payment",payment)
#run





