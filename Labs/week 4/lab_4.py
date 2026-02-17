#Task 1

prices = [1200, 850, 4300, 2999, 1500, 850]
print(len(prices))
avg=sum(prices)/len(prices)
print(avg)
list=[]
for i in prices:
    if(i>2000):
       list.append(i)
print(list)
prices.sort()
print(prices)

#Task 2

locations = [
    (24.8607, 67.0011),
    (31.5204, 74.3587),
    (33.6844, 73.0479)
]
for pair in locations:
    print(pair)
count = len(locations)
print(count)

for loc in locations:
    print(loc[0])
''' print[0]=(23,56)
it gives an error "'builtin_function_or_method' object does not support item assignment "
because tuple is immutable we cannot make any modification in tuple'''

#Task 3

python_students = {"Ali", "Sara", "Ahmed", "Zain"}
ml_students = {"Sara", "Hassan", "Ali", "Fatima"}

both_courses = python_students.intersection(ml_students)
print("Both courses:", both_courses)

only_python = python_students.difference(ml_students)
print("Only Python:", only_python)

all_students = python_students.union(ml_students)
print("All students:", all_students)

ml_students.add("Usman")
print("Updated ML students:", ml_students)

#Task 4

employees = {
    "E01": {"name": "Ali", "salary": 60000},
    "E02": {"name": "Sara", "salary": 75000},
    "E03": {"name": "Ahmed", "salary": 50000}
}

print("Employee IDs:")
for emp_id in employees:
    print(emp_id)

total = 0
for data in employees.values():
    total += data["salary"]

print("Total payroll:", total)

print("Above 60000 salary:")
for emp_id, data in employees.items():
    if data["salary"] > 60000:
        print(data["name"])

employees["E04"] = {"name": "Zain", "salary": 68000}

print("Updated employees:", employees)

#Task 5

sales_data = {
    "electronics": [
        ("Laptop", 120000, 3),
        ("Mouse", 1500, 10)
    ],
    "clothing": [
        ("Shirt", 2500, 5),
        ("Shoes", 5000, 2)
    ]
}

revenue_by_category = {}

for category, items in sales_data.items():
    total = 0
    for product, price, qty in items:
        total += price * qty
    revenue_by_category[category] = total

unique_products = set()

for items in sales_data.values():
    for product, price, qty in items:
        unique_products.add(product)

print("=== Revenue Report ===")

for category, revenue in revenue_by_category.items():
    print(f"{category}: {revenue}")

print("\nUnique Products:", unique_products)

#Extra Question

inventory = {}

unique_products = set()

def add_product(category, name, price, qty):
    if category not in inventory:
        inventory[category] = []
    
    existing_names = {p[0] for p in inventory[category]}
    if name in existing_names:
        print(f"{name} already exists in {category}")
        return
    
    inventory[category].append((name, price, qty))
    unique_products.add(name)

def update_quantity(category, name, new_qty):
    if category in inventory:
        new_list = []
        for product, price, qty in inventory[category]:
            if product == name:
                new_list.append((product, price, new_qty))
            else:
                new_list.append((product, price, qty))
        inventory[category] = new_list

def remove_sold_out():
    for category in inventory:
        inventory[category] = [
            (p, pr, q) for (p, pr, q) in inventory[category] if q > 0
        ]
def generate_report():
    report = {}
    for category, items in inventory.items():
        total_value = 0
        for name, price, qty in items:
            total_value += price * qty
        report[category] = total_value
    return report

add_product("electronics", "Laptop", 120000, 3)
add_product("electronics", "Mouse", 1500, 10)

add_product("clothing", "Shirt", 2500, 5)
add_product("clothing", "Shoes", 5000, 2)

add_product("groceries", "Milk", 200, 20)

update_quantity("electronics", "Mouse", 5)

update_quantity("clothing", "Shoes", 0)

remove_sold_out()

report = generate_report()

print("Final Inventory:")
print(inventory)

print("\nReport:")
print(report)

print("\nUnique Products:")
print(unique_products)
