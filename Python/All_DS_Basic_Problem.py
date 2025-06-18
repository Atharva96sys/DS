# Q1

list1 = [1,2,3,4,5]
newlist = [list1[x] for x in range(len(list1)-1,-1,-1)]
print(newlist)

# Q2
mylist = []
k = 2
mylist = [list1[x] for x in range(k+1,len(list1))]

print(list1)
for x in range(len(list1)-1,k,-1):
    list1.pop(x)

print(mylist+list1)

# Q3
list2 = [5,7,2,3,2,4,6,5]

mylist2 = []

for x in list2:
    if x in mylist2:
        pass
    else:
        mylist2.append(x)

print(mylist2)

# Q4
mylist3 = [1,2,3,4,5,6]
mylist3_square = [x**2 for x in mylist3]
print(mylist3_square)

# Q5
listcu = [1,2,2,3,4,4,5]
print(listcu)
myset = set(listcu)
print(len(myset))

# Q6

setA = {1,2,3,4}
setB = {3,4,5,6}

setC = setA & setB

setD = setA | setB

print(setC)
print(setD)

# Q7
A = {1,2,3,4}
B = {3,4,5}

C = A - (A&B)

print(C)

# Q8

str = "data science is fun and data is power"
listo = list(str.split())

dicti = {}

for x in listo:
    if x in dicti:
        dicti[x] += 1
    else:
        dicti[x] = 1

print(dicti)

# Q9

d = {'a': 3, 'b': 1, 'c': 5} 
sorted_dict = sorted(d.items(),reverse=True)
print(sorted_dict)

# Q10

dict7 = {'a':1,'b':2,'c':3}

key = list(dict7.keys())

values = list(dict7.values())

newdict7 = dict(zip(values,key))

print(newdict7)


