# Program to swap two numbers

num1 = input("Enter num1 : ")
num2 = input("Enter the num2 : ")

print("Before swapping :")
print("Num1 = "+num1)
print("NUm2 = "+num2)

temp = num1
num1 = num2
num2 = temp

print("After swapping :")
print("Num1 = "+num1)
print("Num2 = "+num2)

# Output : 
#         Enter num1 : 51 
#         Enter the num2 : 98
# 
#         Before swapping :
#         Num1 = 51
#         Num2 = 98
# 
#         After swapping :
#         Num1 = 98
#         Num2 = 51