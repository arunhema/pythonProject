# Lists are written as comma separated elements enclosed in square brackets
# list_ex = ['Data']
"""
# An Empty list
MyList = []
print(MyList, "and length is ", len(MyList))

# Adding elements to an empty list
# APPEND adds a Single Element
MyList.append(1)
print(MyList, "and length is ", len(MyList))

# EXTEND adds multiple Elements
MyList.extend([1,2,3,4])
print(MyList, "and length is ", len(MyList))

############################################################################################################
# a Compound elements based list (compound = elements with various data types)
CompoundList = [1, 100, 'a', 'ZZ', 57, 23.7, '@@#']

print (CompoundList)

CompoundList.insert(0,99)
print (CompoundList)

CompoundList.append('pgm')
print (CompoundList)
CompoundList[7] = 767
print (CompoundList)

del CompoundList[3]
print (CompoundList)

############################################################################################################
# Slicing a LIST using indexes
# -----------------------------
masterList = [1, 2, 3, 4, 5, 6]


# 1. Print a part of the list, Slicing a list using ":" operator
#    Also note this Ignores the last INDEX.
print('Slicing a list using ":" operator ' ,masterList[1:5])
# OUTPUT:  Slicing a list using ":" operator  [2, 3, 4, 5]


# 2. Print for a index to end of string
print('Print masterList elements from index 2 (position(3) to end of string ', masterList[2:]);

# 3. Update elements in a list for a given range
masterList [1:4] = ['New1', 'New2', 'New3']
print('Updated masterList: ' ,masterList)

############################################################################################################
# Create a new set "S1"
set1 = {1,2,3,4}
print(set1)

# Create a SET "s1" from a LIST of STRING datatype elements
s1 = set(["USA", "CHINA", "INDIA",])
print(s1)

# Add an element to a set using the ADD function
s1.add("RUSSIA")
print(s1)
s1.add("RUSSIA")
print(s1)

## >## Frozen Sets or Immutable Sets
## >* Frozen sets cannot be changed, once created, they can only be read.
## >* Below is a demonstration of a Mutable or changable set.
## >```
FS1 = frozenset([1,2,3])
print(FS1)

# The below commented code will result in error, As elements cannot be
# added to FROZEN sets
#FS1.add(5)
## >```



## >### Set Operations UNION
## >* Combine SETS with the UNION function
## >* This can be done using **UNION function** or the **| operator**
## >```
# Combine SETS with the UNION function
S1 = {1,2,3}
S2 = {"A", "B", "C",5}

# Create S3 by Merging set S2 with S1 using UNION function
S3 = S1.union(S2)
print(S3)

# Create S3 by Merging set S2 with S1 using | operator
S3 = S1 | S2
print(S3)
## >```

## >### Set Operations INTERSECT
## >* Get common elements between TWO sets using the **INTERSECT function**
## >```
S11 = {1,2,3}
S12 = {1,4,5}
print(S11.intersection(S12))
## >```


## >### Set Operations DIFFERENCE
## >* The **DIFFERENCE FUNCTION** gets the elements not in one over the another
## >* The **- operator** also supports this action.
## >```
print(S11.difference(S12))
print(S12.difference(S11))
## >```


## >### Set Operations Symmetric DIFFERENCE
## >* The **Symmetric DIFFERENCE** will get all differences between both sets
## >* This is done using the **^** operator
## >```

print(S11 ^ S12)

############################################################################################################
# CREATE TUPLE
tuple1 = (1, 2, 3, 4)
tuple2 = ('A', 'b', 1, 2)

# PRINT TUPLE
print(tuple1)
print(tuple2)

print (int(True))
print (int(False))

print ("*********************This is LIST*********************")
list_ex = [1,2,'a','A',"a","!@#",True,1]
print (type(list_ex),len(list_ex))
for i in list_ex: print("Elements value in list:", i,type(i),list_ex.index(i))



print ("*********************This is SET*********************")

set_ex = {1,2,'a','A',"a","!@#",True,1}
print (type(set_ex),len(set_ex))
print(set_ex)
for set in set_ex:
    print(set)
#print(set_ex[2])
print ("*********************This is TUPLE*********************")

tuple_ex = (1,2,'a','A',"a","!@#",True,1)
print (type(tuple_ex),len(tuple_ex))
for i in tuple_ex: print("Elements value in tuple:", i,type(i),tuple_ex.index(i))

print(tuple_ex[7])


S11 = {1,2,3}
S12 = {12,2,3,4,5}
print(S11.union(S12))
print(S12.union(S11))
print(S11 | S12)
print(S12 | S11)




print(S11.intersection(S12))
print(S11.difference(S12))
print(S12.difference(S11))

print(S12 ^ S11)



S1 = {1,2,3}
S2 = {"A", "B", "C"}

# Create S3 by Merging set S2 with S1 using UNION function
S3 = S1.union(S2)
print(S3)

# Create S3 by Merging set S2 with S1 using | operator
S3 = S1 | S2
print(S3)


eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE',1:"ONE"}
print (len(eats))

print(eats[1])

for eat in eats:
    print (eat, eats[eat])

"""
emp_data = [{'EmpNo':1,
             'EmpName':'Arun',
             'EmpSal':100,
             'Proj':[1,6]},
            {'EmpNo':2,
             'EmpName':'Hema',
             'EmpSal':200,
             'Proj':[1,6,"dev"]},
            {'EmpNo':3,
             'EmpName':'HemaArun',
             'EmpSal':30000,
             'Proj':[1,6,77]}
            ]
# i=j=1
# for emp in emp_data:
#     #print ("i = ",i)
#     for proj in emp['Proj']:
#      #   print("j = ",j)
#       #  j = j + 1
#         if proj == 77:
#             print (emp['EmpName'])
#
#     i=i+1

for emp in emp_data:
    #print(emp)
    #print(emp['Proj'])

    for project in emp['Proj']:
        print(project)
        if project == 77:
            print(emp['EmpName'])



"""
def sum(a,b):
    print ("Sum of first num + Second Num is ",(a+b))

print("First num :")
x=int(input())
print("Second num :")
y=int(input())

sum(x,y)
"""