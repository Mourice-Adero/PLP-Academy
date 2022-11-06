salary = float(input('Enter Salary: '))
serviceYears = int(input('Enter service years: '))
if(serviceYears>5):
    bonus = (5/100*salary)
else:
    bonus = 0
print(bonus)