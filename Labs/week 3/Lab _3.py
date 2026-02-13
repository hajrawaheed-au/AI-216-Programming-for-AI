# Task 1
def clean_data(readings):
    cleaned = []
    for value in readings:
        if 0 <= value <= 100:
            cleaned.append(value)
    return cleaned

def calculate_average(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

sensor_readings = [45, 78, -12, 90, 105, 66, 88]

cleaned = clean_data(sensor_readings)
avg = calculate_average(cleaned)

print("Cleaned Data:", cleaned)
print("Average:", avg)

#Task 2

def average_marks(marks):
    return sum(marks) / len(marks)

def has_passed(avg):
    return avg >= 50

def student_summary(name, marks):
    avg = average_marks(marks)
    status = "Pass" if has_passed(avg) else "Fail"
    print(f"{name}  Average: {avg:.2f}, Status: {status}")

students = {
    "Ali": [65, 70, 80],
    "Sara": [90, 85, 88],
    "Ahmed": [40, 55, 60]
}

for name, marks in students.items():
    student_summary(name, marks)

#Task 3

class Dataset:
    def __init__(self, values):
        self.values = values
    
    def count(self):
        return len(self.values)
    
    def average(self):
        return sum(self.values) / len(self.values)

data_values = [12, 18, 25, 30, 22, 27]

data = Dataset(data_values)

print("Count:", data.count())
print("Average:", data.average())

#Task 4

class Classifier:
    def __init__(self, threshold):
        self.threshold = threshold
    
    def classify_one(self, value):
        return value >= self.threshold
    
    def classify_list(self, values):
        results = []
        for v in values:
            results.append(self.classify_one(v))
        return results

threshold = 60
values = [45, 72, 88, 30, 65]

clf = Classifier(threshold)

print(clf.classify_list(values))

#Task 5

def clean_data(data):
    return [x for x in data if 0 <= x <= 100]


class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)
    
    def average(self):
        return sum(self.data) / len(self.data)

raw_data = [10, 55, -3, 78, 120, 66, 92]

cleaned = clean_data(raw_data)
analyzer = DataAnalyzer(cleaned)

print("Cleaned:", cleaned)
print("Count:", analyzer.count())
print("Average:", analyzer.average())


