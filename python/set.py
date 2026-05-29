# >>>>>> set
sat = {1,2,3,5}
print("this is my first set:-",sat)
print("type of my set:-",type(sat))
print("len pf my set:-",len(sat))

sat.remove(1)  # we use it to remove the element of the set(we write element which we want to delete)
print(sat)

#sat.remove("hello")  # give error if the given element is not in 
#sat.discard(1)  # this not give the error while passing the any element which is not in set
#print(sat)