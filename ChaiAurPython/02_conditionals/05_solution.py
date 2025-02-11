'''Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).'''

weather=input("Enter the weather :")
if weather=="Sunny":
    activity="Go for walk"
elif weather=="Rainy":
    activity="Read a Book"
elif weather=="Snowy":
    activity="Build a snowman"
print(activity)