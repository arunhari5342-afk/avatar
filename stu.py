students = []
for i in range(5):
    name = input("Enter Name: ")
    marks = [int(input("Mark1: ")),
             int(input("Mark2: ")),
             int(input("Mark3: ")),
             int(input("Mark4: ")),
             int(input("Mark5: "))]

    students.append({"name": name, "total": sum(marks)})
print("\nStudent Details")
for s in students:
    print(s["name"], "-", s["total"])
high = max(students, key=lambda x: x["total"])
print("\nHighest:", high["name"], high["total"])
low = min(students, key=lambda x: x["total"])
print("Lowest:", low["name"], low["total"])
search = input("\nEnter name to search: ")
for s in students:
    if s["name"] == search:
        print("Found:", s)
print("\nSorted by Marks")
students.sort(key=lambda x: x["total"], reverse=True)
for s in students:
    print(s["name"], s["total"])
print("\nTotal Students:", len(students))
