# Problem: Keep asking the user for input until they enter a number between 1 and 10.

user_input=int(input("Enter a No :"))

if (user_input<=10 and user_input>=1) :
    print(user_input)
else:
    while(user_input <1 or user_input>10):
        print("Please enter a Number between :1 to 10")
        user_input=int(input("Enter the no again :"))
    print(user_input)
