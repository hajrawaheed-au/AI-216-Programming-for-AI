#Problem_1
# Dataset

students_data = [
    {"id": "S01", "name": "Ali", "scores": (78, 85, 90)},
    {"id": "S02", "name": "Sara", "scores": (88, 92, 79)},
    {"id": "S03", "name": "Ahmed", "scores": (45, 60, 55)},
    {"id": "S04", "name": "Zain", "scores": (95, 91, 89)}
]

# Part A – Functional Design

def calculate_average(scores):
    return sum(scores) / len(scores)


def determine_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


def get_top_student(students):
    top_student = None
    highest_avg = -1

    for student in students:
        avg = calculate_average(student["scores"])
        if avg > highest_avg:
            highest_avg = avg
            top_student = student

    return top_student


def get_passed_students(students):
    return [
        student for student in students
        if all(score >= 50 for score in student["scores"])
    ]

# Part B – OOP Design

class StudentAnalytics:

    def __init__(self, students_data):
        self.students_data = students_data

    def compute_results(self):
        for student in self.students_data:
            avg = calculate_average(student["scores"])
            grade = determine_grade(avg)
            student["average"] = avg
            student["grade"] = grade

    def get_top_student(self):
        return max(self.students_data, key=lambda s: s["average"])

    def get_class_average(self):
        total = sum(student["average"] for student in self.students_data)
        return total / len(self.students_data)

    def get_unique_grades(self):
        return {student["grade"] for student in self.students_data}

    def generate_report(self):
        grade_distribution = {}

        for student in self.students_data:
            grade = student["grade"]
            grade_distribution[grade] = grade_distribution.get(grade, 0) + 1

        return {
            "class_average": self.get_class_average(),
            "top_student": self.get_top_student()["name"],
            "grade_distribution": grade_distribution
        }

    #  Consistently Improving Students
    def get_consistently_improving_students(self):
        improving = []

        for student in self.students_data:
            s = student["scores"]
            if s[0] < s[1] < s[2]:
                improving.append(student["name"])

        return improving

    #  Convert to Tabular Structure
    def to_tabular_structure(self):
        table = {
            "ids": [],
            "names": [],
            "averages": [],
            "grades": []
        }

        for student in self.students_data:
            table["ids"].append(student["id"])
            table["names"].append(student["name"])
            table["averages"].append(student["average"])
            table["grades"].append(student["grade"])

        return table

if __name__ == "__main__":
    analytics = StudentAnalytics(students_data)
    analytics.compute_results()

    print("Top Student:", analytics.get_top_student())
    print("Class Average:", analytics.get_class_average())
    print("Unique Grades:", analytics.get_unique_grades())
    print("Report:", analytics.generate_report())
    print("Improving Students:", analytics.get_consistently_improving_students())
    print("Tabular Structure:", analytics.to_tabular_structure())
    
 #Problem 2
    
courses_data = {
    "Python": {
        "instructor": "Dr. A",
        "students": {"S01", "S02", "S03"}
    },
    "Machine Learning": {
        "instructor": "Dr. B",
        "students": {"S02", "S04"}
    },
    "Data Science": {
        "instructor": "Dr. C",
        "students": {"S01", "S04"}
    }
}
# Part A – Functional Design

def get_multi_course_students(courses):
    student_count = {}

    for course in courses.values():
        for student in course["students"]:
            student_count[student] = student_count.get(student, 0) + 1

    return [s for s, count in student_count.items() if count > 1]


def get_large_courses(courses):
    return [name for name, data in courses.items()
            if len(data["students"]) > 2]


def get_student_course_count(courses):
    student_count = {}

    for course in courses.values():
        for student in course["students"]:
            student_count[student] = student_count.get(student, 0) + 1

    return student_count


def get_all_unique_students(courses):
    all_students = set()

    for course in courses.values():
        all_students.update(course["students"])

    return all_students

# Part B – OOP Design
class CourseAnalytics:

    def __init__(self, courses_data):
        self.courses_data = courses_data

    def get_multi_course_students(self):
        return get_multi_course_students(self.courses_data)

    def get_student_course_count(self):
        return get_student_course_count(self.courses_data)

    def get_largest_course(self):
        return max(
            self.courses_data,
            key=lambda c: len(self.courses_data[c]["students"])
        )

    def generate_course_report(self):
        return {
            "total_courses": len(self.courses_data),
            "total_unique_students": len(get_all_unique_students(self.courses_data)),
            "largest_course": self.get_largest_course(),
            "student_course_distribution": self.get_student_course_count()
        }

    #  Convert to Student-Centered Structure
    
    def to_student_centered(self):
        student_structure = {}

        for course_name, data in self.courses_data.items():
            for student in data["students"]:
                if student not in student_structure:
                    student_structure[student] = []
                student_structure[student].append(course_name)

        return student_structure
    
if __name__ == "__main__":
    course_analytics = CourseAnalytics(courses_data)

    print("Multi-course Students:", course_analytics.get_multi_course_students())
    print("Largest Course:", course_analytics.get_largest_course())
    print("Course Report:", course_analytics.generate_course_report())
    print("Student-Centered Structure:", course_analytics.to_student_centered())