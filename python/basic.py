print("hello")
print("123hello")

x = 10
y = "priya" 
print(type(x))
print(type(y))

x = y = z = 10
print(x)
print(y)
print(z)
x = "A"
y = "B"
z = "C"
print(x)
print(y) 
print(z)


#variable :-#VARIABLE -- variables are containers for storing data values.
#a variable name must start with a letter or the underscore character
#a variable name can onlly contqain alpha numeric characters and underscores 
#a variable name cannot start with a number
#a variable names are case sensitive ( age ,Age and AGE are thr4e different variables)
#this means uppercase and lowercase letters are treated as diferent variables. 
#a variable name cannot be any of the python keywords. 

myvar = "john"
my_var = "john"
_my_var = "john"
myvar = "john"
MYVAR = "john"
myvar = "john"
#print() pretty flexible you can enter
print(34)
print("salman khan")
#print(salman khan) not intillized so error
print("swati",23,55,5,True)
print("swati",55,"priya")

print("hello", end="-")
print("world")

print("hello"); print("how are you"); print("i am fine")
print(x,y,z)

#dynamic binding == in python there is no fix datatype before giving value

a = 45
print(a)

a = "divya"
print(a)

a = int('5')  #str->int
print("a")
print(type(a))       #casting

##many values to many varible -- python allows you to assign values to multiple varibles in one line
 
x,y,z = "apple","orange", "mango"
print(x)
print(y)
print(z)

x = y = z = "orange"
print(x)
print(y)
print(z)

#unpack a collection-- if you have a collection of values in a list, tuple etc.
# python allows you can to extract the values into varibles.
#list unpacking

a = ["priya","apple","juice"]
x,y,z = a
print(x)
print(y)
print(z)

#tuple unpack
x = (3,4,5)
a,b,c = a
print(a,b,c)

#string unpack
name = "ABC"
a,b,c = name
print(a,b,c)

x ="python"
y = "is" 
z = "good"
print(x,y,z)

x = "python"
y = "is"
z = "good"
print(x+y+z) #not have space between words

#type casting -- if you  want to specify the datatype of a varible, this can be done with type casting
x = int(3)
y = float(3)
z= str(3)
print(x)
print(y)
print(type(z))

## Type conversion --- you can convert from one type to another with the int(), float(),string()
#1. implict type conversion-- internally know the type

print(6+5.8)
print(type(5),type(5.8))

#.2 explict type conversion -- programe req to change dtype
x = float(20)
print(x)

# user input---
# static vs dynamic software --- static dont talk with user they only gives information
## dynamic -- user input data hai (ex -- youtube, ola, zomato)

a = input("what is your name:")
b = input("what is your age:")
print(a)
print(b)

a = int(input("enter a first number:"))   # have to define 
b = int(input("enter a second number:"))
c = a+b
print(c)

name = input("apna naam batao:")
print("hello",name)

a = int(input("enter a number"))
b = int(input("enter a second number"))
sum = a*b
print("total",sum)

# swap two numbers program
a = 20
b = 13
a,b = b,a
print("A:",a)
print("B:",b)

a = 20
b = 19
c = 5
a,b,c = c,a,b
print("A:",a)
print("B:",b)
print("C:",c)


# string rules--
# .1- sequence of character written inside quotes 
#.2 - include  letters, numbers and spaces
#.3 - strings are immutable/unchanged
#.4 - but we can manipulate strings use methods like concentenationslicing,formating
#.5 - delete an entire string varible (python not possible to delete individual chartar

a = 'hello'
print(a)

c = "python is good"
print(b)
c ='''hey how are you 
sb acha
main thik hu'''
print(c)


