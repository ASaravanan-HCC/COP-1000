# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here

# Calculating state withholding tax at 6.5%
stateTax = salary * 0.065

# Calculating federal withholding tax at 28.0%
federalTax = salary * 0.28

# Calculating dependent deductions at 2.5% of the employee’s salary for each dependent
dependentDeduction = salary * 0.025 * numDependents

# Calculating total withholding as stateTax + federalTax + dependentDeduction
totalWithholding = stateTax + federalTax + dependentDeduction

# Calculating take-home pay as salary - totalWithholding
takeHomePay = salary - totalWithholding

# output statements
print("State Tax : $" + str(round(stateTax, 2)))
print("Federal Tax : $" + str(round(federalTax, 2)))
print("Dependents : $" + str(round(dependentDeduction, 2)))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
