# 1) Create a list with following project IDs 101, 102, 103, 104, 105
# 2) Print all the element in one single line
# 3) Print each element in one line with for loop

# 4) Create a dictionay with emp no, name, salary, projects. Note: Project should be list of all project that employee worked before
# 5) Print key and data of above dictionary
# 6) Print emp name and project they worked one by one

# 7) Create Employee database list with element of type dictionary like #4
# 8) Print key and data of above dictionary
# 9) Print employee names of those who worked on project 103

# 1) Create a list with following project IDs 101, 102, 103, 104, 105
projects = [101, 102, 103, 104, 105]

print("\n# 2) Print all the element in one single line")
print(projects)

print("\n# 3) Print each element in one line with for loop")
for project in projects:
    print(project)

# 4) Create a dictionay with emp no, name, salary, projects. Note: Project should be list of all project that employee worked before
empOne = {'EmpNo':1,'EmpName':'Arun','EmpSal':10000,'EmpProject':[101, 102, 103]}

print("\n# 5) Print key and data of above dictionary")
for emp1 in empOne:
    print(emp1,empOne[emp1])

print("\n# 6) Print emp name and prjoect they worked one by one")
for project in empOne['EmpProject']:
    print (empOne['EmpName'],project)

# 7) Create Employee database list with element of type dictionary like #4
empData =  [{'EmpNo':1,'EmpName':'Hema','EmpSal':10000,'EmpProject':[101, 102, 103]},
            {'EmpNo':2,'EmpName':'Arun','EmpSal':20000,'EmpProject':[102, 104, 105]},
            {'EmpNo':3,'EmpName':'John','EmpSal':30000,'EmpProject':[101, 104, 105]},
            {'EmpNo':4,'EmpName':'Mike','EmpSal':40000,'EmpProject':[103, 104, 105]}
            ]

print("\n# 8) Print key and data of above dictionary")
for emp in empData:
    for data in emp:
        print(data, emp[data])

print("\n# 9) Print employee names of those who worked on project 103")

print ("Enter the project ID for which you need emp Name")
projectID = int(input())

for emp in empData:
    for project in emp["EmpProject"]:
        if project == projectID:
            print (emp["EmpName"])
