'''Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).'''
password=input("Enter Your Password: ")
if len(password) < 6:
    check="Weak"
elif len(password)  <= 10:
    check="Medium"
else:
    check="Hard"
print("Password is",check)