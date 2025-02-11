#Problem: Compute the factorial of a number using a while loop.

number=int(input("Enter a number :"))
if number<0:print("Factorial of neg no is not defined "),exit()
fact=1
i=1
while(i<=number):
    fact=fact*i
    i+=1

print("Factorial of ",number,"is",fact)
