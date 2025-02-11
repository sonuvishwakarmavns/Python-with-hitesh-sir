# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    # print(*args)
    # print(type(*args))
    # for i in args:
    #     print(args,end=" ")
    return sum(args)

print(sum_all(1))
print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4))

# note *args you can chose anything name you want
#print(args):print data in tupple form
# *args type is <class 'int'>
