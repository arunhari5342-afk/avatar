file = open("employees.txt", "a")
emp_id = input("Enter ID: ")
name = input("Enter Name: ")
dept = input("Enter Department: ")
salary = input("Enter Salary: ")
file.write(emp_id + "," + name + "," + dept + "," + salary + "\n")
file.close()
print("Employee added!\n")
file = open("employees.txt", "r")
print("Employee List:")
for line in file:
    print(line.strip())
file.close()
search = input("\nEnter name to search: ")
file = open("employees.txt", "r")
found = False
for line in file:
    data = line.strip().split(",")
    if data[1].lower() == search.lower():
        print("Found:", data)
        found = True
        break
file.close()
if not found:
    print("Employee not found")