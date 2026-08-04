import os
import json
from typing import Dict, List, Optional, Any
from src.entities.student_entitie import Student, Faculty, Grade
from src.use_case.interface.interface import StudentRepo


REPOSITORY_FILE = "src/interface_adapter/repositories/student_repo.json"


class InMemoryRepository(StudentRepo):
    def __init__(self, file_path:str=REPOSITORY_FILE):
        self.file_path = file_path
        self._student_store:List[Dict[str, Student]] = self._chargeStudent()

    def addStudent(self, student:Student) -> Optional[Student]:
        student_dict  = self._toDict(student)
        if self._saveStudent(student_dict):
            return student
        return None

    def deleteStudent(self, id:int) -> bool:
        for s in self._student_store:
            if s["id"] == id:
                self._student_store.remove(s)
                self._saveChange()
                return True
        return False
        
    def getStudentByID(self, id:int) -> Optional[Student]:
        for s in self._student_store:
            if s["id"] == id:
                return self._fromDict(s)
        return None

    def getStudentByName(self, firstname:str, lastname:str) -> Optional[Student]:
        for s in self._student_store:
            if s["firstname"] == firstname and s["lastname"] == lastname:
                return self._fromDict(s)
        return None

    def getAllStudent(self) -> List[Student]:
        students = []
        for s in self._student_store:
            students.append(self._fromDict(s))
            return students
        return []

    def getAllStudentByFaculte(self, faculte:Faculty) -> List[Student]:
        students = []
        for s in self._student_store:
            if s["faculty"] == faculte.value:
                students.append(self._fromDict(s))
                return students
        return []

    def getAllStudentByGrade(self, grade:Grade) -> List[Student]:
        students = []
        for s in self._student_store:
            if s["grade"] == grade.value:
                students.append(self._fromDict(s))
                return students
        return []

    def getAllStudentByFacultyGrade(self, faculte:Faculty, grade:Grade) -> List[Student]:
        students = []
        for s in self._student_store:
            if s["faculty"] == faculte.value and s["grade"] == grade.value:
                students.append(self._fromDict(s))
                return students
        return []

    def _chargeStudent(self) -> List[Student]:
        if os.path.exists(self.file):
            with open(self.file_path, "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
                except json.JSONDecodeError:
                    return []
        return []

    def _checkStudentId(self, student:Dict[Student]) -> bool:
        id = student["id"]
        for s in self._student_store:
            if s["id"] == id:
                return False
        return True

    def _saveStudent(self, student:Student) -> bool:
        student_dict = self._toDict(student)
        if self._checkStudentId(student_dict):
            self._student_store.append(student_dict)
            with open(self.file_path, "w") as f:
                json.dump(self._student_store, f, indent=4)
                return True
        return False

    def _saveChange(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self._student_store, f, indent=4)

    def _fromDict(self, student:Dict[Student]) -> Student:
        return Student(
            id=student["id"],
            firstname=student["firstname"],
            firstname=student["lastname"], 
            faculty=Faculty(student["faculty"]), 
            grade=Grade(student["grade"]),
            gpa=student["gpa"] 
        )

    def _toDict(self, student:Student) -> Dict[Student]:
        return {
            "id": student.id,
            "firstname": student.firstname,
            "lastname": student.lastname,
            "faculty": student.faculty.value,
            "grade": student.grade.value,
            "gpa": student.gpa
        }