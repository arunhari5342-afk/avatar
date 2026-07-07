import json
emp = []
class Employee:
    def add(self):
        emp.append({"id":input("ID: "),
                    "name":input("Name: "),
                    "salary":int(input("Salary: "))})

    def view(self):
        for i in emp:
            print(i)

    def search(self):
        x=input("Enter ID: ")
        for i in emp:
            if i["id"]==x:
                print(i)
                return
        print("Not Found")

    def update(self):
        x=input("Enter ID: ")
        for i in emp:
            if i["id"]==x:
                i["salary"]=int(input("New Salary: "))
                print("Updated")
                return
        print("Not Found")

    def delete(self):
        x=input("Enter ID: ")
        for i in emp:
            if i["id"]==x:
                emp.remove(i)
                print("Deleted")
                return
        print("Not Found")

    def save(self):
        with open("emp.json","w") as f:
            json.dump(emp,f)
        print("Saved")

    def load(self):
        global emp
        try:
            with open("emp.json","r") as f:
                emp=json.load(f)
            print("Loaded")
        except FileNotFoundError:
            print("File Not Found")

e=Employee()

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Save 7.Load 8.Exit")

    try:
        ch=int(input("Choice: "))

        if ch==1:
            e.add()
        elif ch==2:
            e.view()
        elif ch==3:
            e.search()
        elif ch==4:
            e.update()
        elif ch==5:
            e.delete()
        elif ch==6:
            e.save()
        elif ch==7:
            e.load()
        elif ch==8:
            break
        else:
            print("Invalid Choice")

    except ValueError:
        print("Enter numbers only.")
