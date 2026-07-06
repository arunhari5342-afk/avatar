height = float(input("enter the height:"))
weight = float(input("enter the weight:"))
bmi = weight/(height*height)
print("your bmi is:",bmi)
if bmi<18.5:
    print("category:underweight")
elif bmi<25:
    print("category:normalweight")
elif bmi<30:
    print("category:overweight")
else:
    print("category:obese")
