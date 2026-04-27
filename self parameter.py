class Employee:
    language = "Py"# This is a class attribute
    salary = 120000
    
    def getInfo(self):
        print(f"The language is{self.language}. The salaray is {self.salary}")

harry = Employee()
harry.language = "JavaScript" # This is a instance attribute 
harry.getInfo()
# employee.getInfo(harry)