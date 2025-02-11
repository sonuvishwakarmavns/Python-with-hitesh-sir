age=int(input("Enter Your age :"))
day="Wednesday"

price=12 if age>=18 else 8

if day=="Wednesday":
    price-=2

print("price of ticket is $",price)