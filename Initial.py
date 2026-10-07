from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grades: list[int]

    @property
    def average(self) -> float:
        return sum(self.grades) / len(self.grades)


class StudentManager:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, name: str, grades: list[int]):
        self.students.append(Student(name, grades))

    def top_students(self, limit: int = 3):
        return sorted(
            self.students,
            key=lambda student: student.average,
            reverse=True
        )[:limit]

    def show_report(self):
        print("Student Report")
        print("==============")

        for student in sorted(
            self.students,
            key=lambda item: item.average,
            reverse=True
        ):
            print(
                f"{student.name} | "
                f"Grades: {student.grades} | "
                f"Average: {student.average:.2f}"
            )


manager = StudentManager()

manager.add_student("Alex", [92, 88, 95, 90])
manager.add_student("Sarah", [100, 94, 97, 99])
manager.add_student("Michael", [78, 85, 82, 80])
manager.add_student("Emma", [91, 93, 89, 96])
manager.add_student("Daniel", [84, 79, 88, 86])

manager.show_report()

print("\nTop Students")
print("------------")

for student in manager.top_students():
    print(f"{student.name}: {student.average:.2f}")