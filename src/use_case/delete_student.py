from dataclasses import dataclass
from src.entities.student_entitie import Student, Faculte, Grade
from src.use_case.interface.interface import StudentRepo
from typing import Optional


DEL_ERR_MESSAGE = "Student not found"
DEL_SUCC_MESSAGE = "Student has been deleted succesfully"




@dataclass
class DeleteStudentInput:
    id : int

@dataclass
class DeleteStudentOuput:
    message : str
    status : bool


class DeleteStudent:
    def __init__(self, repository : StudentRepo):
        self.repository = repository

    def execute(self, input_data : DeleteStudentInput) -> DeleteStudentOuput:
        deleted = self.repository.deleteStudent(input_data.id)
        if not deleted:
            return DeleteStudentOuput(
                message = DEL_ERR_MESSAGE,
                status = False
            )
        else: 
            return DeleteStudentOuput(
                message = DEL_SUCC_MESSAGE,
                status = True
            )