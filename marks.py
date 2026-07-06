a = int(input("Enter your physics mark: "))
b = int(input("Enter your maths mark: "))
c = int(input("Enter your chemistry mark: "))
d = int(input("Enter your biology mark: "))
e = int(input("Enter your english mark: "))
f = int(input("Enter your tamil mark: "))
total = a + b + c + d + e + f
average = total / 6
percentage = total / 6
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")