# string rules--
# .1- sequence of character written inside quotes 
#.2 - include  letters, numbers and spaces
#.3 - strings are immutable/unchanged
#.4 - but we can manipulate strings use methods like concentenationslicing,formating
#.5 - delete an entire string varible (python not possible to delete individual chartar

a = 'hello'
print(a)

b = "python is good"
print(b)
c ='''hey how are you 
sb acha
main thik hu'''
print(c)

name = "sapna"
print("My name is:-",name)

print("type of my variable:- ",type(name))
# type function type check karne ke kam aata hai

print("len of my string:-",len(name))   #tell characters of the string
upper_case =name.upper() #upper is used to convert  all elements into upper case
print(upper_case)

lower_case = name.lower()  #convert all elements in lowercase
print(lower_case)

name ="RAHUL"
print(name.casefold())  # same work as lower case

## task-1  Difference between lower() and casefold()
# a ="Straße" 
# print(a.lower()) # lower print only normal language
# b = "Straße"
# print(b.casefold()) # casefold prints multi language into  lower and dont't change in english

#task2- what is difference between title and capitalized
name ="dev"
print(name.title())  # first letter captial of every word in a paragraph

print(name.capitalize()) # first letter of first word  of a paragraph

# task-3 different ways to reverse a string python
name  = "priya"
print(name[::-1])

#task-4 whether the strip() can remove spaces between words inside a string

name ="upflairs  "  # jab koi string ke aage ya peeche space jada ho tho woh bhi length m count hote hai
print(len(name))  # toh unko hatane ke liye strip ka use karte hai
print(name.strip()) # lekene strip beeche wale space nhi haata 

intro =  "hello hi kya kar rehe ho , tum thik ho"

# # #indexing and slicing
# # print(name[2])
# # print(name[2:8])

# # #slicing
# # print(name[-1]) #shows last element of string
##postion +1 and indexing -1



# # name = "priya"
# # last_name = "shekhawat"
# # print(name+last_name)  ## + join

# # print(name +"  "+ last_name) # we can add space after this.

str1 = "garima"
str2 = "agarwal"
#print(str1 * str1) # this not print this is not valid
#print(str1 + str1) # run and print name two times
print(str1 + str2) 
# print(str1 + 2) # this not print
print(str1 * 2) # this also give output
#print(str1 * str2) # this is cannot happen because this not valid

name = 'dev'
name = "dev"

#task5 what is difference between this single quotes and double quotes for strings in python
#

intro = "hello my name is priya"
intro1 = "hello my \n name is \n priya" # jaha jaha apn ko list k element divide karne ho wah wah \n use kare
 
print(intro)
print(intro1.split()) # intr1 string thi lekin split karne ke bhaad list m save hota h

name = "govind"
address = "jodpur" #f is used to do formatting
print(f"my name is {name} and i from {address}") # f is used to define the variable in between the string in print


 #input function is used to take input from the user
name = input("enter your name :-")
print(name)
print(type(name))

number1 =int(input("enter you first number:-"))
number2 =int(input("enter second number:- "))
print(number1,number2)
print(type(number1))
print(type(number2))