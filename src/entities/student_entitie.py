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
    FINISHED = "Finished"


@dataclass
class Student:
    firstname : str
    lastname : str
    faculty : Faculty
    id : str
    photo : str 
    grade : Grade = Grade.PREP
    gpa : str = "0"

    def __post_init__(self):
        if not self.id:
            raise InvalideData("no id")
        if not self.firstname.strip():
            raise InvalideData(ERR_NAME)
        if not self.lastname.strip():
            raise InvalideData(ERR_NAME)
        
        gpa_value = float(self.gpa)
        if gpa_value < MIN_GPA :
            raise InvalideData(ERR_GPA)
        if gpa_value > MAX_GPA :
            raise InvalideData(ERR_GPA)
        if len(str(self.id)) != ID_SIZE :
            raise InvalideData(ERR_ID)
        
        self.firstname = self.firstname.strip()
        self.lastname = self.lastname.strip()
        self.gpa = f"{gpa_value:.2f}"

    def _in_prep(self) -> bool:
        return self.grade == Grade.PREP

    def validateGrade(self, grade:Grade) -> bool:
        if self.grade == Grade.PREP and grade == Grade.FRESHMAN:
            return True
        elif self.grade == Grade.FRESHMAN and grade == Grade.SOFOMORE:
            return True
        elif self.grade == Grade.SOFOMORE and grade == Grade.JUNIOR:
            return True
        elif self.grade == Grade.JUNIOR and grade == Grade.SENIOR:
            return True
        elif self.grade == Grade.SENIOR and grade == Grade.FINISHED:
            return True
        else:
            return False
        
        