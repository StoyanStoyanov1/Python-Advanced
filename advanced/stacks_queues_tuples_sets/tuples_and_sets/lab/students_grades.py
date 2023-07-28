class StudentsGrades:
    students_grades = {}

    def __init__(self, students):
        self.students = students
        self.for_each_student()

    def for_each_student(self):
        for current_student in self.students:
            current_student = current_student.split()
            student = current_student[0]
            grade = float(current_student[1])
            if student not in self.students_grades:
                self.students_grades[student] = []
            self.students_grades[student].append(grade)

    def __repr__(self):
        result = []
        for name, grades in self.students_grades.items():
            grades_in_string = list(map(lambda grade: str(f"{grade:.2f}"), grades))
            average_grade = str(f"{sum(grades) / len(grades):.2f}")
            result.append(f"{name} -> {' '.join(grades_in_string)} (avg: {average_grade})")

        return "\n".join(result)


students = tuple(input() for _ in range(int(input())))
print(StudentsGrades(students))
