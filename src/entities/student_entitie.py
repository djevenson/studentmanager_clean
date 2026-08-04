from dataclasses import dataclass, field
from enum import Enum


MAX_GPA = 4.00
MIN_GPA = 0.00
ID_SIZE = 10
ERR_NAME = "Name connot be empty"
ERR_GPA = f"GPA shoud be in {MIN_GPA} - {MAX_GPA}"
ERR_ID = f"ID shoud have {ID_SIZE} characters"


class InvalideData(Exception):
    pass


class Faculty(Enum):
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
    faculty : Faculty
    grade : Grade
    gpa : float = field(default_factory=0.00)

    def __post_init__(self):
        if not self.firstname.strip():
            raise InvalideData(ERR_NAME)
        if not self.lastname.strip():
            raise InvalideData(ERR_NAME)
        if self.gpa < MIN_GPA :
            raise InvalideData(ERR_GPA)
        if self.gpa > MAX_GPA :
            raise InvalideData(ERR_GPA)
        if len(str(self.id)) != ID_SIZE :
            raise InvalideData(ERR_ID)
        self.id = float(self.id)
        self.firstname = self.firstname.strip()
        self.lastname = self.lastname.strip()
      