class Employee:
    def __init__(self, emp_id, emp_name, department, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Department:", self.department)
        print("Salary:", self.salary)

   def update_salary(self, new_salary):
        self.salary = new_salary
        print("Salary updated successfully.")

    def display_annual_salary(self):
        annual_salary = self.salary * 12
        print("Annual Salary:", annual_salary)

emp1 = Employee(101, "Rajesh", "Computer", 70000)
emp1.display()
emp1.update_salary(75000)
emp1.display()

# Display annual salary
emp1.display_annual_salary()
