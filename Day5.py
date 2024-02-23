# F-Strings => It is an enhanced string concatination technoque by avoiding the "+" and using f as a prefix 
#           => And putting variables in curly braces Eg:f"this is an example {Variables} of f-strings"
#           => NO need for type casting (Converting to string for concatination)

# Sample Program : 
name = "Aromal"
age = 20
print(f"Hello..!I'm {name} and I'm {age} years old")


# Conditional Statements

#  =>Simple if else
#  Syntax : 
#         if condition :       => paranthesis() not necessary for condition
#                 statements
#         else :
#              statements

# Sample program 1:

smaple_age = int(input("Fact check..! Enter your Age :"))

if smaple_age >= 18 :
    print("You are eligible for Voting..")
else :
    print("Not eligible..")

# # Sample Program 2:

num = int(input("Enter a Positive integer :"))
if (num % 2 == 0):
    print("Even")
else :
    print("Odd")



# =>Nested if 

# Sample Program :

another_age = int(input("Enter your age :"))
height = float(input("Enter your height in meters :"))
if(height >= 1) :
    print("You are permitted for this rollerCoster")
    if(another_age <= 18) :
        print("You must pay $500")
    else :
        print("You Must pay $250")
else :
    print("You are not permitted")



# if elif(else if) Ladder

# Syntax:
# if(condition 1):
#        statement 1
# elif(condition 2):
#         statement 2
# elif(condition 3):
#          statement 3
# .......
# else:
#        statement n

# Sample Program:
print("Enter 1 for addition and 2 for subtraction and 3 for multiplication and 4 for division")
ch = int(input("Enter your choice :"))

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

if(ch == 1):
    res = num1+num2
    print(f"The sum is :{res}")
elif(ch == 2):
    res = num1 - num2
    print(f"The result is :{res}")
elif(ch == 3):
    res = num1*num2
    print(f"The result is :{res}")
elif(ch == 4):
    res = num1/num2
    print(f"The result is :{res}")
else:
    print("Invalid choice..")
