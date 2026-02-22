#Problem 1

rent=float(input("Enter your monthly rent:"))
food=float(input("Enter your monthly food expenses:"))
transport=float(input("Enter your montly Transport expenses:"))
utilities=float(input("Enter your monthly utility expenses:"))

budget_limit= 60000
total_expense= rent + food + transport + utilities
print(f"Your total monthly expense is: {total_expense } pkr")

if(total_expense<=budget_limit):
    print("Within Budget")
else:
    print("Over Budget")
    
#Problem 2

units_consumed=float(input("Enter the units consumed this month:"))
print(f"you have consumed {units_consumed} units this month")

if (units_consumed<=100):
    print("Basic Rate")
elif(101<=units_consumed<=300):
    print("Standard Rate")
else:
    print("High Usage Rate")
    
    
#problem 3

attendance_list=[72, 85, 90, 60, 40, 78, 88]
regular_students=0
short_attendance=0

for i in attendance_list:
    if(i>=75):
        regular_students+=1
    else:
        short_attendance+=1
    
print(f"{regular_students} students are regular")
print(f"{short_attendance} students have short attendance")


#Problem 4
cgpas = [3.6, 3.2, 3.8, 3.5, 3.0]
incomes = [75000, 90000, 60000, 80000, 70000]

eligible = 0

for i in range(5):
    if cgpas[i] >= 3.5 and incomes[i] <= 80000:
        eligible += 1

print("Total eligible students:", eligible)


#Problem 5

readings = [10, 25, 50, 85, 70, 15, 90, 40]

alerts = 0

for r in readings:
    if r < 20 or r > 80:
        alerts += 1

total = len(readings)
percentage = (alerts / total) * 100

print("Total alerts:", alerts)
print("Alert percentage:", percentage, "%")
