# dictionary
 #dict is mutable and have duplicate value and have unique key
student = {"name":"Priya",
           "class":"third year",
           "Roll number":29,
           "branch":"cse",
           "Address":"siker"}
# name,class,roll no, branch,address >>>>>> keys
# Priya,third year,29,cse,siker
# key + value = "items"
# print(student)
# print("dict keys",student.keys())
# print("dict values",student.values())
# print("dict item",student.items())

print(student["name"])
print(student["class"])
print(student["branch"])

# for adding items in dict
# student["subject"]= "python"
# print(student)
# task1 use addend function
# task2 use from key

# print(student.get("name"))  # get function give the value of key
# print(student.clear()) 
# print(student.clear("name")) # shows error
# print(student.copy())
# print(student.pop("name"))
# print(student.popitem())  # popitems show(pop) the last item

car = { "brand":"kia",
         "model": "seltos",
         " year": 2000}

print(car)
x = car.setdefault("colour","black") 
print(x)

# deep copy and copy difference  task 2

car = { "brand": ["kia","hero","honda","maruti"],
       "model": "seltos",
         " year": 2000}
# print(car)
# car["year"]= 2005 # for update the value of any key without any predefined function
# print(car)

for x in car.keys():
    print(x)
for x in car.values():
    print(x)
for x in car.items():
    print(x)   
    
