from typing import Counter


lower=int(input("lower limit:"))
upper=int(input("upper input :"))

for x in range(lower, upper+1):
    if(x%2)!=0 :
        print(x, end=" ")

#COUNTER
counter=1
max=3

while counter<max:
    print(counter)
    counter=counter+1

#show multiple
x=20
while x>20 :
    if(x%3)==0:
        print(x,end=" ")
    x=x-1
    
