# Creating List 

my_list = [10,20,40,"Hey",3.65,[8,8,4]]

# Creating List Using list()

my_list2 = list(range(10))
my_list3 = list([x for x in my_list[1:3:2]])
print(my_list[10:])
print()
print(my_list2)
print(my_list3)

# Access Element From List

print(my_list[5])

a = my_list2[-2]

print(a)

# Adding Element into List

my_list2.append(6)
my_list2.extend([2,5,2])
my_list2.insert(8,1)

print(my_list2)

# Updating List
my_list2[8] = 0

#Removing Element From List

my_list2.remove(8)
print(my_list2)

# Exception Handling
try:
    my_list2.remove(8)
except:
    print("Invalid Operation")

# Popping Element From list
b=my_list.pop(3)
print(my_list)
print(b)

# Deleting Element From List
print(my_list2)

del my_list2[3]

print(my_list2)
# Taking Single Input From User
# w = input("Enter")

# Taking List As Input From User
# rye = input("Enter").split()
# print(rye)


# List Concatenation
my_list4 = my_list2+my_list3

print(my_list4)


my_list5 = [[6,3,8,2,0],[9,2,4,6,7]]

for i in my_list5:
    for j in i:
        print(j, end=' ')
    print()

#Nested List
a = my_list5[0][0]
print(a)

for x in range(len(my_list2)):
    print(my_list2[x])


#List Comprehension

quwu = [x for x in my_list if type(x) == int or type(x) == float]

print(quwu)


