'''Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]'''


number=[1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count=0

#First method
for i in range(len(number)):
    if number[i]>0:
        count+=1
print(count)

#second method
count=0
for i in number:
    if (i > 0):
        count=count+1
print("positive no in list is",count)
