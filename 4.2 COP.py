# Get input from the user
employeeName = input("Enter the employee's name: ")
numShifts = int(input("Enter the number of shifts: "))
numTransactions = int(input("Enter the number of transactions: "))
transactionValue = float(input("Enter the transaction dollar value: "))

# Calculate productivity score
productivityScore = (transactionValue / numTransactions) / numShifts

# Determine bonus based on productivity score
if productivityScore <= 30:
    bonus = 50.0
else:
    if 31 <= productivityScore <= 69:
        bonus = 75.0
    else:
        if 70 <= productivityScore <= 199:
            bonus = 100.0
        else:  # productivity_score >= 200
            bonus = 200.0

# Output the results
print(f"Employee Name: {employeeName}")
print(f"Employee Bonus: ${bonus}")
