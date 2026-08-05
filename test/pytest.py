import os
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from dataclasses import dataclass, field
from enum import Enum


MAX_GPA = 4.00
MIN_GPA = 0.00
ID_SIZE = 10
file="test/test.json"


class InvalideData(Exception):
    pass


class Faculte(Enum):
    CE = "Civil ingeneering"
    GA = "Agronomy"
    BA = "Business administration"
    CS = "Computer science"


class Grade(Enum):
    PREP = "1st grade"
    FRESHMAN = "2nd grade"
    SOFOMORE = "3nd grade"
    JUNIOR = "4th grade"
    SENIOR = "5th grade"


@dataclass
class Student:
    id : int
    firstname : str
    lastname : str
    faculty : Faculte
    grade : Grade
    gpa : float = field(default_factory=0)

    def __post_init__(self):
        if not self.firstname.strip():
            raise InvalideData("Firstname connot be empty")
        if not self.lastname.strip():
            raise InvalideData("Lastname connot be empty")
        if self.gpa < MIN_GPA :
            raise InvalideData(f"GPA cannot be less than {MIN_GPA}")
        if self.gpa > MAX_GPA :
            raise InvalideData(f"GPA cannot be greater than {MAX_GPA}")
        
        self.firstname = self.firstname.strip()
        self.lastname = self.lastname.strip()  


def _chargeStudent() -> List[Any]:
        if os.path.exists(file):
            with open(file, "r") as f:
                try:
                    data =json.load(f)
                    if isinstance(data, list):
                        return data
                except json.JSONDecodeError:
                    return []
        return []

students:List[Dict[str, Any]] = _chargeStudent()


def _checkStudentId(student:Dict[Student]):
    id = student["id"]
    for s in students:
        if s["id"] == id:
            return False
    return True
        


def _toDict(student:Student) -> Dict[Student]:
    return {
        "id": student.id,
        "firstname": student.firstname,
        "lastname": student.lastname,
        "faculty": student.faculty.value,
        "grade": student.grade.value,
        "gpa": student.gpa
    }


def _saveStudent(student:Student):
    student_dit = _toDict(student)
    if not _checkStudentId(student_dit):
        print("student already exists")
        return
    students.append(student_dit)
    with open(file, "w") as f:
        json.dump(students, f, indent=4)

def _saveChange() -> None:
    with open(file, "w") as f:
        json.dump(students, f, indent=4)

def deleteStudent(id:int) -> bool:
    for s in students:
        if s["id"] == id:
            students.remove(s)
            _saveChange()
            return True
    return False


student1 = Student(id=2025040036,firstname="djevenson", lastname="janvier", faculty=Faculte.GA, grade=Grade.SENIOR, gpa=2.14) 
def _toCliRow(student:Student) -> str:
    return f"{student.id:{ID_SIZE+1}} | {student.firstname:<15} | {student.lastname:<15} | {student.faculty.value:<20} | {student.grade.value:10} | {student.gpa}"

def try5():
    #print(_toDict(student1))
    print(_toCliRow(student1))
    print(len(str(student1.faculty.value)))
    print(deleteStudent(202388))
    print(len(str(float(3.550))))

print((float(3.5550)))
#try5()