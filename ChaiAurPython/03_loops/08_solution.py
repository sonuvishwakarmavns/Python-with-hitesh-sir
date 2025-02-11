'''Problem: Check if a number is prime.'''
number=int(input("Enter a Number :"))
if(number<0):print(number,"is not prime") ,exit()
count=0
for i in range(1,number):
    if(number>1):
        if(number%i==0):count+=1
if(count>=2):print(number,"is Not Prime") 
else :print(number,"is Prime")