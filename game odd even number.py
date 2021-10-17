finish=False
while not finish:
    number=int(input("number :"))
    if(number%2==0):
        print("even number")
    else :
        print("odd number")
        
    next=input("again? (Yes/No)")
    if next=="No" :
        finish=True