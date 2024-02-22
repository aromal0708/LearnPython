print("Program to calculate the BMI of a person ")

weight = input("Enter the weight in Kg :")
height = input("Enter your height im Meter :")
age = input("Enter Your Age :")

BMI = int(weight)/(float(height)**2)

# round(int/float variable/value, no of decimal digits) => round off a number

print("Your BMI is :"+str(round(BMI,2)))