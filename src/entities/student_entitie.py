from dataclasses import dataclass, field
from enum import Enum


MAX_GPA = 4.00
MIN_GPA = 0.00


class InvalideData(Exception):
    pass


class Faculte(Enum):
    CE = "Civil ingeneering"
    GA = "Agronomy"
    BA = "Business administration"
    CS = "Computer science"


class Grade(Enum):
    PREP = "First grade"
    FRESHMAN = "Second grade"
    SOFOMORE = "Third grade"
    JUNIOR = "Fourth grade"
    SENIOR = "Fith grade"


@dataclass
class Student:
    id : int
    firstname : str
    lastname : str
    faculty : Faculte
    grade : Grade
    gpa : float = field(default_factory=0.00)

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