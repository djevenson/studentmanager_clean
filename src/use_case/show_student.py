from dataclasses import dataclass, field
from src.entities.student_entitie import Student, Faculty, Grade
from src.use_case.interface.interface import StudentRepo
from typing import Optional, List


@dataclass 
class ShowStudentInput:
    faculty : Optional[Faculty] = None
    grade : Optional[Grade] = None

@dataclass 
class ShowStudentOuput:
    total : int
    faculty : Optional[Faculty] 
    grade : Optional[Grade] 
    students : List[Student] = field(default_factory=list)
    def __post_init__(self) -> None:
        self.total = len(self.students)


class ShowStudent:
    def __init__(self, repository : StudentRepo):
        self.repository=repository
        self.faculty = "ALL"
        self.grade = "ALL"

    def execute(self, input_data : ShowStudentInput) -> ShowStudentOuput:
        
        if not input_data.faculty and not input_data.grade:
            students = self.repository.getAllStudent()
            
        elif not input_data.grade:
            students = self.repository.getAllStudentByFaculty(input_data.faculty)
            self.faculty = input_data.faculty.value

        elif not input_data.faculty:
            students = self.repository.getAllStudentByGrade(input_data.grade)
            self.grade=input_data.grade.value

        else:
            students=self.repository.getAllStudentByFacultyGrade(input_data.faculty, input_data.grade)
            self.faculty=input_data.faculty.value
            self.grade=input_data.grade.value

        students_sorted = sorted(students, key=lambda s: s.lastname, reverse=True)
        return ShowStudentOuput(
            faculty=self.faculty,
            grade=self.grade,
            students=students_sorted,
            total=len(students)

        )