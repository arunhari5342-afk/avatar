employees = []
while True:
    print("\n1.Add  2.View  3.Search  4.Update Salary  5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        emp_id = input("ID: ")
        name = input("Name: ")
        dept = input("Dept: ")
        salary = float(input("Salary: "))
        employees.append([emp_id, name, dept, salary])
        print("Employee added!")
    elif choice == "2":
        for emp in employees:
            print(emp)
    elif choice == "3":
        name = input("Enter name: ")
        found = False
        for emp in employees:
            if emp[1].lower() == name.lower():
                print("Found:", emp)
                found = True
                break
            if not found:
                print("Not found")
    elif choice == "4":
        emp_id = input("Enter ID: ")

        for emp in employees:
            if emp[0] == emp_id:
                emp[3] = float(input("New Salary: "))
                print("Updated!")
                break
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice")