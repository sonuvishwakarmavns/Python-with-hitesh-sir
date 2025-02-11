'''Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)'''

print("Fruit Colors:Green ,Yellow ,Brown")
color=input("Enter the color of Fruit :")
fruit="Banana"
if fruit=="Banana":    
    if color=="Green":
     print("unripe")
    elif color=="Yellow":
        print("Ripe")
    elif color=="Brown":
     print("Overripe")
