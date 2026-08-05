from src.entities.student_entitie import Student, Faculty, Grade, ID_SIZE



class StudentPresenter:
    @staticmethod
    def _toCliRow(student:Student) -> str:
        return f"\
        {student.id:<{ID_SIZE}+1} |\
        {student.firstname:<15} |\
        {student.lastname:<15} |\
        {student.faculty.value:<20} |\
        {student.grade.value:10} |\
        {student.gpa}\
        "
    
    @staticmethod
    def _toCliDetail(student:Student):
        lines = [
            f"ID          : {student.id}",
            f"Firstname   : {student.firstname}",
            f"Lastname    : {student.lastname}",
            f"Faculty     : {student.faculty.value}",
            f"Grade       : {student.grade.value}",
            f"GPA         : {student.gpa}"
        ]
        return "\n".join(lines)

    @staticmethod
    def _facultyToCliOPtion():
        return f"1. {Faculty.CE.value}(CE) | 2. {Faculty.BA.value}(BA) | 3. {Faculty.GA.value}(GA) | 4. {Faculty.CS.value}(CS)"

    @staticmethod
    def _gradeToCliOption():
        return f"1. {Grade.PREP.value} | 2. {Grade.FRESHMAN.value} | 3. {Grade.SOFOMORE.value} | 4 {Grade.JUNIOR.value} | {Grade.SENIOR.value}"



class _C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    CYAN   = "\033[36m"
    RED    = "\033[31m"

    def _banner(text: str) -> None:
        print(f"\n{_C.BOLD}{_C.CYAN}{'=' * 50}{_C.RESET}")
        print(f"{_C.BOLD}{_C.CYAN}  {text}{_C.RESET}")
        print(f"{_C.BOLD}{_C.CYAN}{'=' * 50}{_C.RESET}\n")

    def _ok(msg: str) -> None:
        print(f"{_C.GREEN}  ✓  {msg}{_C.RESET}")

    def _err(msg: str) -> None:
        print(f"{_C.RED}  ✗  {msg}{_C.RESET}")

    def _inval(msg: str) -> str:
        print(f"{_C.YELLOW}  ✗  {msg}{_C.RESET}")