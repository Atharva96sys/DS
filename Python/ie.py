# import sys
# op = [10,20,4,45,99]

# max = sys.maxsize*-1
# smax = sys.maxsize*-1

# for i in op:
#     if i >max:
#         smax = max
#         max = i

# print(smax)

# op1 = [1,2,1,3,4,1]

# a = int(input("Enter Element To Remove From List"))

# newop = []
# for i in op1:
#     if i != a:
#         newop.append(i)

# print(newop)

# sum =0
# for i in op:
#     sum = sum + i
# print(sum)


list = [1,2,3,4]

a = list[len(list)-1]
print(a)

for i in range(len(list)-1):
    list[i+1] = list[i]

list[0]=a
print(list)