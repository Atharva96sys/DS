# Creating Dictionary

dict3 = {
    "name" : "atharva",
    "age" : 20,
    "college" : " ABV-IIITM",
    "subjects" : ["Python","DS","ML"],
}

# Accessing Element By Key

print(dict3["name"])

# Adding And Updating Dictionary Item
dict3["time"] = 9.00

dict3["age"] = 21

print(dict3)

# Creating Empty Dictinary

dictN = {}

dictN["name"] = "Sawant"

print(dictN)

# Nested dict3
#   Value --> dict3{}
dict2 = {
    "name":"SGHD",
    "subject":{
        "phy":89,"chem":92,"maths":94
    }
}
print(dict2["subject"]["phy"])

# Dictionary Methods
print(dict3.keys()) # Returns all keys in form of list know as dict3 keys

print(dict3.values()) # Returns All Values in form of list know as dict3 values

print(dict3.items()) # Returns All Item eg key:value pair in form of tuples 

print(dict3.get("name")) # Same As dict3["name"]

'''Difference Is dict3["name2"] will give error if "name2" key is not in 
  dictionary but dict3.get("name2) will not give error only it will print message
'''
# If Error Will Occur This Will prevent system to being shut down


dict3.update({"city":"nashik"}) # Updated dict3 


# Also This Function Can Take Multiple dict3 Item At Ones

dict4 = {"pincode":422012,"bill number":"3228NM3IOA18P2"}
dict3.update(dict4)

print(dict3)

dict5 = {1:'abc',2:'brt',3:'cop'}

# Value Length in Dictionary

# Method 1
    # Using loop + len()

mydict = {1:'gfg',2:'is',3:'best'}

res = {value:len(value) for value in mydict.values()}

print(res)


from collections import Counter

str = "data science is fun and data is power"

frequency  = Counter(str.split())

frequency_dict = dict(frequency)

print(frequency_dict)

str1 = "data science is fun and data is power"

words = str.split()

frequency1 = {}

for word in words:
    if word in frequency1:
        frequency1[word] += 1
    else:
        frequency1[word] = 1

print(frequency1)