c = "Hello" #String Declaration

print("hello 'world'") #Printing String

a = "Atharva"
b = '''ueuiv
xbc xdhcddde
wycdyujvb jhbhe
vgdydjrfb''' # Multi Line String Declaration

# You Can also use double quotes to declare string

print(b) # Printing MultiLine String


# Strings Are Arrays Of Character or Bytes Representing Unicode
Str = "QWERTYUIOP"
ty = Str[3] # You Can Access Element Or Character In String Using Sqaure Brackets
print(ty) # Output:- R

# Looping Throught String 
for i in Str:
    print(i)
# Output:- Q W E R T Y U I O P  Every Character On Different Line

#len() function is used to get length of given string
print(len(Str)) #Output:- 10

#Check In String
    # Use in operator to Check If Given String is Present in Main String

print("QWER" in Str) #Prints True
# Note:- When Input A String To Check Individual Character Are Not Check Whole String Is Chek At Ones

print("QRTY" in Str)# Prints False 
    # AS Q R T Y Are Present in string But QRTY Whole Is Not Present 


# Not Operator Used To Invert Given Condition
print("QRTY" not in Str) #Prints Truen


#SLICING Strings

Str1 = "ASDfghjkL"

print(Str1[2:6])# Prints DFGH
# Slicing To Make A SubString
# Str1[:8] --> Slices String From Start To 8
# Str1[2:] --> Slices String From 2 To End

# upper() method converts String to Upper Case
print(Str1.upper())

# lower() method converts String To Lower Case
print(Str1.lower())

# both of them does'nt change original string
print(Str1)