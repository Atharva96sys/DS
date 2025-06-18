fruits = ["apple","banana","grapes"]
#Looping In List 
for x in fruits:
    print(x)
#Prints All Element From List "fruits"

a = "Atharva"
# Looping in string
for x in a:
    print(x)
#prints all character on new line from string "a"

#break and continue is used same as other language uses

for x in fruits:
    if x == "banana":
        break
    print(x)

# Breaks Loop When x contains "banana"

'''Range Function Used To Give A Sequence Of Number
with given starting point and end before point with 
manual increament (default 1)'''

for x in range(0,25,2):
    print(x)
# First Index Is Starting Point From Where Number Generation Starts
# Second Index Is End Point To Before Which NUmber Should Stop Generating
# Third Index Is Increament Value, by which current value is increamented to get next number in sequence


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished: