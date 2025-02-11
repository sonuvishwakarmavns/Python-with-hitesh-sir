# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item=set()
#set does not contain any duplecate value
for item in items:
    if item in unique_item:
        print("Duplecate",item)
        break
    unique_item.add(item)