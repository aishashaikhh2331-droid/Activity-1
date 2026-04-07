# student_management.py

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # list of marks

    def get_average(self):
        total = 0
        for g in self.grades:
            total += g
        return total / len(self.grades)  # BUG: ZeroDivisionError if grades is empty

    def get_grade_letter(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70
            return "C"   # BUG: missing colon above
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def is_eligible_for_scholarship(self):
        if self.get_grade_letter == "A":  # BUG: forgot () - comparing method not result
            if self.age =< 20:           # BUG: invalid operator, should be <=
                return True
        return False


def process_students(student_list):
    results = []
    for student in student_list:
        info = {
            "name": student.name,
            "average": student.get_average(),
            "grade": student.get_grade_letter(),
            "scholarship": student.is_eligible_for_scholarship()
        }
        results.append(info)
    return results


def find_topper(student_list):
    topper = None
    for student in student_list:
        if topper is None or student.get_average() > topper.get_average()
            topper = student   # BUG: missing colon above
    return topper.name  # BUG: crashes if student_list is empty


def save_results(results, filename):
    file = open(filename, "w")
    for r in results:
        file.write(str(r) + "\n")
    # BUG: file is never closed


# Main
students = [
    Student("Tanu", 20, [85, 90, 78]),
    Student("Priya", 19, []),       # BUG: empty grades will crash get_average
    Student("Riya", 21, [70, 65])
]

topper = find_topper(students)
print("Topper:", topper)

results = process_students(students)
save_results(results, "output.txt")
