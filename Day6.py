# Lists in Python => Collection of multiple data which can be of same/diff data types in a single variable  I
#                 =>It is a dynamically allocated arrays

# syntax : 
#         names  = ["Name1","Name2","Name3"] 
#         rollno = [34,1,50,56,45,25]

# Sample Program :
names  = ["Aromal","Aaromal","Devan","Evan","Binosh","Amal"] 
rollno = [34,1,50,56,45,25]

print(names)
print(rollno)
print(len(rollno)) #To print the length of the List

print(rollno[1:3]) #Slicing the array =>[FirstIndex:The end length(0,1,2)] =>Output :[1,50] 
rollno.sort() #Sort the List =>cannot be applied on a Mixed List (Only applicable for List of same data type)
print(rollno)

# append(value) =>is used to append a value to the end of the List
names.append("Dan")
rollno.append(49)
print(names)
print(rollno)

#insert(index,value) =>used to insert a value at a desired position

names.insert(0,"Elbin")
rollno.insert(0,55)

print(names)
print(rollno)

# remove(value) => Used to remive an element from a List
# pop(index/nothing) =>remove the last/arguement index element and it returns the


# Nested List => List within a List
# Example : [[1,23,34],[2,3,4],["Arun","Akash","Arohi"]]

