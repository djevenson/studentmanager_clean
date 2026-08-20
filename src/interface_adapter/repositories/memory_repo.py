import os
import json
from typing import Dict, List, Optional, Any
from src.entities.student_entitie import Student, Faculty, Grade , ID_SIZE
from src.use_case.interface.interface import StudentRepo, StudentIdGeneratorInterface
from datetime import datetime

REPOSITORY_FILE = "src/interface_adapter/repositories/student_repo.json"


class InMemoryRepository(StudentRepo):
    def __init__(self, file_path:str ):
        self.file_path = file_path
        self._student_store:List[Dict[str, Any]] = self._chargeStudent()

    def addStudent(self, student:Student) -> Optional[Student]:
        #student_dict  = self._toDict(student)
        if self._saveStudent(student):
            return student
        return None

    def deleteStudent(self, id:str) -> bool:
        for s in self._student_store:
            if s["id"] == id:
                self._student_store.remove(s)
                self._saveChange()
                return True
        return False
            
    def getStudentByID(self, id:str) -> Optional[Student]:
        for s in self._student_store:
            if s["id"] == id:
                return self._fromDict(s)
        return None

    def getStudentByName(self, firstname:str, lastname:str) -> Optional[Student]:
        for s in self._student_store:
            if s["firstname"].lower() == firstname.lower() and s["lastname"].lower() == lastname.lower():
                return self._fromDict(s)
        return None

    def getAllStudent(self) -> List[Student]:
        students = []
        for s in self._student_store:
            students.append(self._fromDict(s))
        return students

    def getAllStudentByFaculty(self, faculty:Faculty) -> List[Student]:
        students = []
        for s in self._student_store:
            if s["faculty"] == faculty.value:
                students.append(self._fromDict(s))
        return students

    def getAllStudentByGrade(self, grade:Grade) -> List[Student]:
        students = []
        for s in self._student_store:
            if s["grade"] == grade.value:
                students.append(self._fromDict(s))
        return students
        

    def getAllStudentByFacultyGrade(self, faculty:Faculty, grade:Grade) -> List[Student]:
        students = []
        for s in self._student_store:
            if s["faculty"] == faculty.value and s["grade"] == grade.value:
                students.append(self._fromDict(s))
        return students


    def getLastRank(self, prefix:str) -> int:
        matching_ranks = [
            int(s["id"][6:]) for s in self._student_store if s["id"].startswith(prefix) and len(s["id"]) == ID_SIZE
        ]
        return max(matching_ranks, default=0)

    def _chargeStudent(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
                except json.JSONDecodeError:
                    return []
        return []

    def _checkStudentId(self, student:Dict[str, Any]) -> bool:
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

    def _fromDict(self, student:Dict[str, Any]) -> Student:
        return Student(
            id=student["id"],
            firstname=student["firstname"],
            lastname=student["lastname"], 
            faculty=Faculty(student["faculty"]), 
            grade=Grade(student["grade"]),
            gpa=student["gpa"] 
        )

    def _toDict(self, student:Student) -> Dict[str, Any]:
        return {
            "id": student.id,
            "firstname": student.firstname,
            "lastname": student.lastname,
            "faculty": student.faculty.value,
            "grade": student.grade.value,
            "gpa": student.gpa
        }




class InMemoryStudentIdGenerator(StudentIdGeneratorInterface):
    _FACULTY_CODE = {"CE":1, "BA":2, "GA":3, "CS":4}

    def __init__(self, repository: StudentRepo) -> None:
        self._repository = repository

    def generate(self, faculty:Faculty) -> str:
        prefix = f"{datetime.now().year}{self._FACULTY_CODE[faculty.name]:02d}"  
        rank = self._repository.getLastRank(prefix) + 1
        id = f"{prefix}{rank:04d}"
        return id