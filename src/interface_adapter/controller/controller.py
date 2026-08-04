from typing import Dict, Any
from src.use_case.add_student import AddStudent, AddStudentInput
from src.use_case.delete_student import DeleteStudent, DeleteStudentInput
from src.use_case.search_student import SearchStudentByName, SearchStudentById, SearchStudentByIdInput, SearchStudentByNameInput
from src.use_case.show_student import ShowStudentInput, ShowStudent
from src.use_case.interface.interface import StudentRepo



class StudentController:
    def __init__(self, repository:StudentRepo):
        self.add_use_case = AddStudent(repository)
        self.delete_use_case = DeleteStudent(repository)
        self.search_id_use_case = SearchStudentById(repository)
        self.search_name_use_case = SearchStudentByName(repository)
        self.show_use_case = ShowStudent(repository)

    def addStudent(self, input_data:AddStudentInput) -> Dict[str, Any]:
        output_data = self.add_use_case.execute(input_data)
        return {
            "succes": output_data.status,
            "message": output_data.message,
            "student": output_data.student
        }

    def deleteStudent(self, input_data:DeleteStudentInput) -> Dict[str, Any]:
        output_data = self.delete_use_case.execute(input_data)
        return {
            "succes": output_data.status,
            "message": output_data.message
        }

    def searchStudentById(self, input_data:SearchStudentByIdInput) -> Dict[str, Any]:
        output_data = self.search_id_use_case.execute(input_data) 
        return {
            "succes": output_data.status,
            "message": output_data.message,
            "student": output_data.student
        }

    def searchStudentByName(self, input_data:SearchStudentByNameInput) -> Dict[str, Any]:
        output_data = self.search_name_use_case.execute(input_data) 
        return {
            "succes": output_data.status,
            "message": output_data.message,
            "student": output_data.student
        }

    def showStudent(self, input_data:ShowStudentInput) -> Dict[str, Any]:
        output_data = self.show_use_case.execute(input_data)
        return {
            "faculty": output_data.faculty,
            "grade": output_data.grade,
            "students": output_data.students,
            "total": output_data.total
        }