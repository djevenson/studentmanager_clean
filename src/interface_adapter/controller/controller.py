from typing import Dict, Any
from src.use_case.add_student import AddStudent, AddStudentInput
from src.use_case.delete_student import DeleteStudent, DeleteStudentInput
from src.use_case.search_student import SearchStudentByName, SearchStudentById, SearchStudentByIdInput, SearchStudentByNameInput
from src.use_case.show_student import ShowStudentInput, ShowStudent
from src.use_case.interface.interface import StudentRepo
from src.entities.student_entitie import Faculty, Grade


class StudentController:
    def __init__(self, repository:StudentRepo):
        self.add_use_case = AddStudent(repository)
        self.delete_use_case = DeleteStudent(repository)
        self.search_id_use_case = SearchStudentById(repository)
        self.search_name_use_case = SearchStudentByName(repository)
        self.show_use_case = ShowStudent(repository)

    def addStudent(self, id:int, firstname:str, lastname:str, faculty:Faculty, grade:Grade, gpa:float) -> Dict[str, Any]:
        output_data = self.add_use_case.execute(AddStudentInput(
                id=id,
                firstname=firstname,
                lastname=lastname,
                faculty=faculty,
                grade=grade,
                gpa=gpa
            )
        )
        return {
            "succes": output_data.status,
            "message": output_data.message,
            "student": output_data.student
        }

    def deleteStudent(self, id:int) -> Dict[str, Any]:
        output_data = self.delete_use_case.execute(DeleteStudentInput(id=id))
        return {
            "succes": output_data.status,
            "message": output_data.message
        }

    def searchStudentById(self, id:int) -> Dict[str, Any]:
        output_data = self.search_id_use_case.execute(SearchStudentByIdInput(id=id)) 
        return {
            "succes": output_data.status,
            "message": output_data.message,
            "student": output_data.student
        }

    def searchStudentByName(self, firstname:str, lastname:str) -> Dict[str, Any]:
        output_data = self.search_name_use_case.execute(SearchStudentByNameInput(
            firstname=firstname,
            lastname=lastname
            )
        ) 
        return {
            "succes": output_data.status,
            "message": output_data.message,
            "student": output_data.student
        }

    def showStudent(self, faculty:Faculty, grade:Grade) -> Dict[str, Any]:
        output_data = self.show_use_case.execute(ShowStudentInput(
            faculty=faculty,
            grade=grade
            )
        )
        return {
            "faculty": output_data.faculty,
            "grade": output_data.grade,
            "students": output_data.students,
            "total": output_data.total
        }