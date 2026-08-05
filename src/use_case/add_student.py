from dataclasses import dataclass
from src.entities.student_entitie import Student, Faculty, Grade
from src.use_case.interface.interface import StudentRepo
from typing import Optional


ADD_SUCC_MESSAGE = "Student added successfully"
 

@dataclass
class AddStudentInput:
    id : int
    firstname : str
    lastname : str
    faculty : Faculty
    grade : Grade
    gpa : float


@dataclass
class AddStudentOutput:
    student : Optional[Student]
    message : str
    status : bool



class AddStudent:
    def __init__(self, repository:StudentRepo):
        self.repository = repository

    def execute(self, input_data = AddStudentInput) -> AddStudentOutput:
        exist_id = self.repository.getStudentByID(input_data.id)
        if exist_id:
            return AddStudentOutput(
                message = f"Student with ID : '{input_data.id}' already exists",
                student = None,
                status = False
            )
        else:
            try:
                student = Student(
                    id = input_data.id,
                    firstname = input_data.firstname,
                    lastname = input_data.lastname,
                    faculty = input_data.faculty,
                    gpa = input_data.gpa,
                    grade = input_data.grade
            )
            except Exception as e:
                return AddStudentOutput(
                    student = None,
                    message = str(e),
                    status = False
            )

            student = self.repository.addStudent(student)
            return AddStudentOutput(
                student = student,
                message = ADD_SUCC_MESSAGE,
                status = True
            )