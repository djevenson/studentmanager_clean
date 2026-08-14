import os
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

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
    PREP = "1st grade"
    FRESHMAN = "2nd grade"
    SOFOMORE = "3nd grade"
    JUNIOR = "4th grade"
    SENIOR = "5th grade"


@dataclass
class Student:
    firstname : str
    lastname : str
    faculty : Faculty
    id : str = "0"
    grade : Grade = Grade.PREP
    gpa : str = "0"

    def __post_init__(self):
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

def create():
    try:
        s = Student(id="2026020034", firstname="Djevenson", lastname="Janvier", faculty=Faculty.BA)
        print(f"ID: {s.id}\nName: {s.firstname} {s.lastname}\nFaculty: {s.faculty.value}")
        print(datetime.now().year)
    except Exception as e:
        print(e)

create()