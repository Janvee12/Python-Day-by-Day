class Employee:
    language = "Py"# This is a class attribute
    salary = 120000


harry = Employee()
harry.language = "JavaScript" # This is a instance attribute 
print( harry.language, harry.salary)

