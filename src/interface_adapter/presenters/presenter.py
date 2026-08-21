from src.entities.student_entitie import Student, Faculty, Grade, ID_SIZE
from typing import  Dict, Any, List



class StudentPresenter:
    @staticmethod
    def _toDict(student:Student) -> Dict[str, Any]:
        return{
            "ID": student.id,
            "Firstname": student.firstname,
            "Lastname": student.lastname,
            "Photo": student.photo,
            "Faculty": student.faculty.value,
            "Grade": student.grade.value,
            "GPA": student.gpa
        }

    @staticmethod
    def _toListDisct(students: List[Student]) -> List[Dict[str, Any]]:
        return [StudentPresenter._toDict(student) for student in students]

    @staticmethod
    def _toCliTable(students:List[Student]) -> str:
        if len(students) > 0:
            
            print(f"\n{' '*42}STUDENT TABLE{' '*43}")
            print(f"|{'-'*98}|")
            print(f"| {"ID":{ID_SIZE}} | {"Firstname":<15} | {"lastname":<15} | {"Faculty":<24} | {"Grade":13} | {"GPA"}  |")
            print(f"|{'-'*98}|")
            total = 0
            for student in students:
                print(f"| {student.id:{ID_SIZE}} | {student.firstname:<15} | {student.lastname:<15} | {student.faculty.value:<24} | {student.grade.value:13} | {student.gpa:4} |")
                total += 1
            print(f"|{'-'*98}|")
            print(f" TOTAL : {total:4}{' '*85}\n")
    
    @staticmethod
    def _toCliDetail(student:Student):
        lines = [
            f"ID          : {student.id}",
            f"Firstname   : {student.firstname}",
            f"Lastname    : {student.lastname}",
            f"Faculty     : {student.faculty.value}",
            f"Grade       : {student.grade.value}",
            f"GPA         : {student.gpa}\n"
        ]
        return "\n".join(lines)

    @staticmethod
    def _facultyToCliOPtion():
        return f"1. {Faculty.CE.value}(CE) | 2. {Faculty.BA.value}(BA) | 3. {Faculty.GA.value}(GA) | 4. {Faculty.CS.value}(CS)"

    @staticmethod
    def _gradeToCliOption():
        return f"1. {Grade.PREP.value} | 2. {Grade.FRESHMAN.value} | 3. {Grade.SOFOMORE.value} | 4. {Grade.JUNIOR.value} | 5. {Grade.SENIOR.value}"



class _C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    CYAN   = "\033[36m"
    RED    = "\033[31m"

    def _banner(text: str) -> None:
        print(f"\n{_C.BOLD}{_C.CYAN}{'=' * 101}{_C.RESET}")
        print(f"{_C.BOLD}{_C.CYAN}{" " * 20}{text}{_C.RESET}")
        print(f"{_C.BOLD}{_C.CYAN}{'=' * 101}{_C.RESET}\n")

    def _ok(msg: str) -> None:
        print(f"{_C.GREEN}  ✓  {msg}{_C.RESET}")

    def _err(msg: str) -> None:
        print(f"{_C.RED}  ✗  {msg}{_C.RESET}")

    def _inval(msg: str) -> str:
        print(f"{_C.YELLOW}  ✗  {msg}{_C.RESET}")