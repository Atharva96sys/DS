# Tuples In Python Are Same As List In Python With immutablity

# Creating Tuple

a = (1,2,3,4,5,6)

mylist = [5,6,7,8,3]

b = tuple(mylist) # Using List

c =tuple([8,9,4,3]) # Pass Iterable

print(a)
print(b)
print(c)

# Using String

d = ('eyiw','shjf')

print(d)

# Access Element 

print(a[2:6])


print(a[::-1])

# Deleting Tuple

del a

print(tuple(reversed(b)))


# Accessing Values In Python

tup = (8,9,1,4)

print(tup[2])

# Traverse In Tuple

for x in tup:
    print(x,end=" ")

print()

# Concatenation of tuple

tup1 = (3,5)
tup2 = (6,8)
print(tup1+tup2)
print(tuple(tup1+tup2))

# tup1+tup2 --> concatenate tuple in one big tuple        --> (3,5,6,8)
# (tup1,tup2) --> big tuple with two element which are already tuple -->((3,5),(6,8)) 

# Nested Tuples

tup3 = (tup1,tup2)
print(tup3)

# Repetation In Python Tuple

tup4 = (9,)*3

print(tup4)

# Slicing In Tuple Is Same As Slicing In List With Using Square Brackets

print(tup[2:])

# Deleting Tuple We Cannot Remove Element From Tuple But we Can delete whole tuple by using 'del' keyword

del tup3

# print(tup3) # Gives Error On Calling Non existing item

# Converting List To Tuple and vice-versa

lis = [38,7,3,4,9,3,2,3]

tup3 = tuple(lis)

print(tup3)

mylist = list(tup3)

# Tuples In Loop

n = 5
for i in range(n):
    tup = (tup,)
    print(tup)

# Different Ways Of Creating A Tuple

t1 = (5,6,7)
t2 = 5,6,7
t3 = tuple([5,6,7]) # Tuple Constructor Requireds A Iterable Data Type
t4 = () # Empty Tuple
t5 = (5,) 
# Creating A Single Element Tuple 
    # Its Required A Comma for differencating between tuple and other different data types(int,float,string)

# Tuple Packing Unpacking

a,b,c = 5,6,7

tp = (a,b,c)

print(tp)


