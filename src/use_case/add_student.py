from dataclasses import dataclass
from src.entities.student_entitie import Student, Faculty, InvalideData
from src.use_case.interface.interface import StudentRepo, StudentIdGeneratorInterface
from typing import Optional


ADD_SUCC_MESSAGE = "Student added successfully"
 

@dataclass
class AddStudentInput:
    firstname : str
    lastname : str
    faculty : Faculty
   


@dataclass
class AddStudentOutput:
    student : Optional[Student]
    message : str
    status : bool



class AddStudent:
    def __init__(self, repository:StudentRepo, id_generator:StudentIdGeneratorInterface):
        self.repository = repository
        self.id_generator = id_generator

    def execute(self, input_data : AddStudentInput) -> AddStudentOutput:
        generated_id = self.id_generator.generate(input_data.faculty)
        
        try:
            student = Student(
                id = generated_id,
                firstname = input_data.firstname,
                lastname = input_data.lastname,
                faculty = input_data.faculty
        )
        except InvalideData as e:
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