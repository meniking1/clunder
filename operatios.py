from unittest import result

num1= int(input("choose number"))

num2= int(input("coose one more number"))
which_one = input("choose which one(+,-,*,/)")
if which_one == "*":
    print (num1*num2)
elif which_one == "+":
    print(num1+num2)
elif which_one == '/':
    print(num1/num2)
elif which_one== '-':
    print(num1-num2)
else:
    print("sorry i cant understand you.hh")
