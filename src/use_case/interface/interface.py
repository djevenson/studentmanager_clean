from abc import ABC, abstractmethod
from typing import Optional, List
from src.entities.student_entitie import Student, Faculty, Grade

class StudentRepo(ABC):

    @abstractmethod 
    def getStudentByID(self, id : int) -> Optional[Student]:
        ...

    @abstractmethod
    def getStudentByName(self, firstname:str, lastname : str) -> Optional[Student]:
        ...

    @abstractmethod
    def getAllStudent(self) -> List[Student]:
        ...

    @abstractmethod
    def getAllStudentByFaculty(self, faculty : Faculty) -> List[Student]:
        ...

    @abstractmethod
    def getAllStudentByGrade(self, grade : Grade) -> List[Student]:
        ...

    @abstractmethod
    def getAllStudentByFacultyGrade(self, faculty : Faculty, grade : Grade) -> List[Student]:
        ...

    @abstractmethod
    def addStudent(self, student : Student) -> Optional[Student]:
        ...

    @abstractmethod
    def deleteStudent(self, id : int) -> bool:
        ...
