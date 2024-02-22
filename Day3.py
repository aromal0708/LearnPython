# Primitive dataTypes in Python
#           =>int  ->integer values
#           =>float -> floating point numbers with decimal values like "3.14"
#           =>str ->string variables
#           =>bool ->boolean values like True/False  T / F must be in UpperCase

# Sample Program :

variable1 = 234
variable2 = "Hello Im Aromal"
variable3 = 23.5
variable4 = False
variable5 = "a"

print(type(variable1))  #<class 'int'>
print(type(variable2))  #<class 'str'>
print(type(variable3))  #<class 'float'>
print(type(variable4))  #<class 'bool'>
print(type(variable5))  ##<class 'str'>


# Type checking & Type Casting

#  conver to string => str(variable /number /whatever)
# Convert to integer =>int(variable /string /whatever)
# Convert to float =>float(variable /string /whatever)

#Sample program : 

name = input("Enter your name : ")
print("Length of your name is "+str(len(name))+" characters")

# program to add two numbers recieved from a user

num1 = input("Enter the first number :")
num2 = input("Enter the second number :")

res = int(num1)+int(num2)

print("The result is : "+str(res))


# Program to Add digits of a given number (Two digits) :

num = input("Enter a two digit number :")

result = int(num[0])+int(num[1])

print("The result is : "+str(result))
