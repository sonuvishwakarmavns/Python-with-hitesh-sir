'''3. Polymorphism in Functions
Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.'''

def multiply(numOne,numTwo):
    return numOne * numTwo
print(multiply(6,5))
print(multiply(6,"sonu"))
# print(multiply("ram","sonu")) gives an error str*str

