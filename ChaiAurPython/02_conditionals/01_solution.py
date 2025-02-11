age=int(input("Provide Your Age :"))

if(age>100):
    print("please renter age correctly")
    exit()
            

if age<13:
    print("Child")
elif age<19:
    print("Teenager")
elif age<59:
    print("Adult")
else :
    print("Senior")
