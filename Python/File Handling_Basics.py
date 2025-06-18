# Reading A File

f=open("Python/Strings.txt",'r')

print(f.read())
f.close()

# Writing And Appending In File

with open("Python/Strings1.txt",'w') as g:
    g.write("Hello Any Thing New \n")

with open("Python/Strings.txt",'a') as h:
    h.write("hy")


k = open("Python/Strings.txt",'r')
print(k.read())
k.close()

lines = ["Data Science\n","Is\n","Fun\n"]
with open("output.txt",'w') as l:
    l.writelines(lines)

with open("output.txt",'r') as l:
    print(l.read())