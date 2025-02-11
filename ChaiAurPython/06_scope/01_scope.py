# x=99
# def func ():
#     global x
#     x = 15
#     return x

# print(func())

#Closer in python............

def input_num(x):
    def square(num):
        return num**x
    return square

f=input_num(2)#x=3

print(f(3))#num
    
