from dataclasses import dataclass
from src.entities.student_entitie import Student
from src.use_case.interface.interface import StudentRepo
from typing import Optional, List


SEARCH_SUCCESS_MESSAGE = "There is the student"
SEARCH_ECHEC_MESSAGE = "Student not found"

@dataclass
class SearchStudentByIdInput:
    id : int


@dataclass
class SearchStudentByNameInput:
    firstname : str
    lastname : str
    def __post_init__(self):
        self.firstname = self.firstname.strip()
        self.lastname = self.lastname.strip()


@dataclass
class SearchStudentOutput:
    message : str
    status : bool
    student : Optional[Student] = None




class SearchStudentById:
    def __init__(self, repository : StudentRepo):
        self.repositoy = repository

    def execute(self, input_data : SearchStudentByIdInput) -> SearchStudentOutput:
        student = self.repositoy.getStudentByID(input_data.id)
        if not student :
            return SearchStudentOutput(
                message = SEARCH_ECHEC_MESSAGE,
                status = False
        )
        else:
            return SearchStudentOutput(
                message = SEARCH_SUCCESS_MESSAGE,
                student = student,
                status = True
        )




class SearchStudentByName:
    def __init__(self, repository : StudentRepo):
        self.repositoy = repository

    def execute(self, input_data : SearchStudentByNameInput) -> SearchStudentOutput:
        student = self.repositoy.getStudentByName(input_data.firstname, input_data.lastname)
        if not student :
            return SearchStudentOutput(
                message = SEARCH_ECHEC_MESSAGE,
                status = False
        )
        else:
            return SearchStudentOutput(
                message = SEARCH_SUCCESS_MESSAGE,
                student = student,
                status = True
        )