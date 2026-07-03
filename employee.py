class Employee:
    def __init__(self,emp_id,emp_name,department,salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.salary = salary
    def display(self):
        print("Employee id:", self.emp_id)
        print("Employee name:", self.emp_name)
        print("department:", self.department)
        print("salary:", self.salary)
emp1=Employee(101,"rajesh","computer",70000)
emp1.display()