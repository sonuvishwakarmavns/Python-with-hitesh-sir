#Problem: Reverse a string using a loop.
# string concatination
'''
    i=0 string[0]=S
    rev_str=i+rev_str
    print(type(i))
    <class 'str'>
    //concatination
    rev_str=0+S
-------------------------
    i=1 string[1]=o
    rev=1+S
    rev=oS
'''

string="Sonu"
rev_string=""
for i in string:
    #rev_string=rev_string + i #same same like sonu swap (i pahle aur revstring baad me string rev ho jayegi)
    rev_string=i+rev_string 
print(rev_string)




   