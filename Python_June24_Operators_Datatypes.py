

#Artametic Operators

print(1+3)

#Assignment - assign data to a variable
firstname = "Krishna"
#firstname = firstname + "Chaitanya"
firstname += "Chaitanya"

a=3
a *= 2

print(firstname) # in b/w text + will join string

#Comparision- Compare 2/ more values -> True/ False
#Used in conditional statements
#== != <, >, <=, >=

a=25
b=100
print(a<=b)

#Logical Operators: Combine conditional statements.
#O/p: True/ false

# and, or, not
# and -> All conditions True -> True
# or -> Any one condition true -> True
# not -> reverse condition value-> True->False, False-> True

a=10

print(not(a>1 and a<0))

#Bitwise operators
#1->0001 8421
#2->0010

print(5&4)
#0101
#0100
#------
#0100
#-----


#membership operator: Check specific value/ item exists in the given list/ string.
#True/ False
# in, not in
email ="krishna@gmail.com"
print(('@' in email) and ('.com' in email))

emails = ["meena@gmail.com", "praneth@gmail.com", "sabeer@gmail.com"]
email ="meena@gmail.com"
print(email in emails)

#Identity operators: 2 varaibles rererring to same address or not
#Datatype-> Value, Reference
#is, is not
a=1
b=a
print(a is b)
#All the data types in python treated as object type.

print(type(a))

#Check data type of a variable: Using type() keyword.
a=1
print(type(a))
#Outpur: <class 'int'>

#Data Type: specify data type of a varaible.
"""
1. Number/ Numeric- Int, float, complex
"""
a=12313213.31312
print(type(a))

"""
a+bj-Estimated value
"""
a=1+2j
b=1-3j
print(a+b)

"""
2. String: char/string
"""
name ="Krishna"

"""
Boolean data type: True/ False
"""
a= True
print(type(a))

"""
None-Nothing. Create a varaible without data.
"""
salary=None
print(type(salary))


