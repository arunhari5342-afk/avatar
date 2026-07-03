basic_salary = float(input("enter your basic salary:"))
hra = basic_salary*0.20
da = basic_salary*0.10
ta = basic_salary*0.5
pf = basic_salary*0.12
tax = basic_salary*0.8
total_allowances = hra+da+ta
total_deductions = pf+tax
net_salary = basic_salary+total_allowances-total_deductions
print("basic salary:",basic_salary)
print("HRA:",hra)
print("DA:",da)
print("TA:",ta)
print("TOTAL ALLOWANCE:",total_allowances)
print("PF:",pf)
print("TAX:",tax)
print("TOTAL DEDUCTIONS:",total_deductions)
print("NET SALARY:",net_salary)