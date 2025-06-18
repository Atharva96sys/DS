# File.txt:
# QWERTYUIOP 
# QWERTYUI RTYHN

# Q1

with open("Python\File.txt",'r') as q:
    list1 = q.readlines()
    print(len(list1))
# Q2

with open("Python\File.txt",'r') as h:
    stry = h.read()
    print(stry)

with open("Python\File2.txt",'w') as r:
    r.write(stry.upper())

print()
with open("Python\File2.txt",'r') as y:
    print(y.read())

# Q3
a = input()
with open("Python\File4.txt",'w') as k:
    k.write(str(a))
# Q4

listw = ["My ","Name ","Is ","Lakhan"]

with open("Python\File3.txt",'a') as f:
    for x in listw:
        f.write(str(x))
        f.write("\n")


