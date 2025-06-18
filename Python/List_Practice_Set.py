a = [1,2,3,4,5]
a.reverse()
print(a)

b = [7,22,1,-3,14]

max = b[0]
min = 37282
for i in range(len(b)):
    if max < b[i]:
        max = b[i]
for i in range(len(b)):
    if min > b[i]:
        min = b[i]

print(max)
print(min)

# for x in range(5):
#     b.append(input("Enter"))

# print(b)
count = 0
for i in [1,2,3,1,1,4]:
    if i == 1:
        count += 1

print(count)


res = [val for val in [1,2,3,4,5,6] if val%2 == 0]
print(res)


sq = [val*val for val in range(1,11) ]

print(sq)
o = [1,2,2,3,4,4,4]


la = input("Enter List").spilt()

print(la)
