# Loops :

# for loop 
# Syntax :
#        for item in iteratible:
#                   statements...

# Smaple program:
numbers = [1,23,34,45,67]
sum = 0
for num in numbers :
    sum+=num

print(f"The sum is {sum}")


# While Loop :

# Syntax :
#       while condition :
#                 statements...

# Sample Program :
count = 0
limit = int(input("Enter the num till you want to print numbers"))

while count <= limit :
    print(count)  #print from 1 to 100
    count+=1
print("Out of while loop")