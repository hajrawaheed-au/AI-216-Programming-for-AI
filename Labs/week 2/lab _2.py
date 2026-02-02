#Task 1

food = 500
transport = 300
stationery = 200

# Calculate total
total_expense = food + transport + stationery


budget = 1500

print("Total daily expense:", total_expense, "PKR")

if total_expense > budget:
    print("Budget exceeded!")
else:
    print("Within budget! ")
    
#Task 2

a=int(input("Enter data usage in GB:"))
if (a<=5):
   Package=" Basic Package"
elif(a>=6 and a<=15):
    Package= "Standard package"
else:
    Package= "Premium Package"

print("Recommended Package: ",Package)

#Task 3


temperatures = [12, 18, 25, 31, 29, 35, 22, 30, 33]

normal_count = 0
high_count = 0

for temp in temperatures:
    if 15 <= temp <= 30:
        normal_count += 1
    elif temp > 30:
        high_count += 1

print("Normal readings:", normal_count)
print("High readings:", high_count)

#Task 4:

incomes = [70000, 50000, 65000]
statuses = ["Employed", "Unemployed", "Employed"]

count = 0


for i in range(3):
    if incomes[i] >= 60000 and statuses[i] == "Employed":
        count = count + 1

print("Eligible applicants:", count)


#Task 5

speeds = [60, 85, 90, 70, 82, 75, 95]

violations = 0


for s in speeds:
    if s > 80:
        violations += 1

percentage =( (violations /len(speeds))*100 )

print("Total violations:", violations)
print("Violation percentage:", percentage, "%")

