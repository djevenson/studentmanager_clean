from src.interface_adapter.presenters.presenter import StudentPresenter, _C
from src.interface_adapter.repositories.memory_repo import InMemoryRepository
from src.interface_adapter.controller.controller import StudentController
from src.entities.student_entitie import Faculty, Grade, ERR_GPA, ERR_ID, ERR_NAME, MAX_GPA, MIN_GPA



REPOSITORY_FILE = "src/interface_adapter/repositories/student_repo.json"
COMMANDS = "Commands: 1. add | 2. list | 3. search by id | 4. search by name | 5. delete | 0. quit"



def _chooseFaculty() -> Faculty:
    print(StudentPresenter._facultyToCliOPtion())
    while True:
        cmd = input(f"{_C.BOLD}> {_C.RESET}").strip().lower()
        if cmd.lower().strip() in ("1",f"{Faculty.CE.value.lower()}", "ce"):
            return Faculty.CE
        elif cmd.lower().strip() in ("2",f"{Faculty.BA.value.lower()}", "ba"):
            return Faculty.BA
        elif cmd.lower().strip() in ("3",f"{Faculty.GA.value.lower()}", "ga"):
            return Faculty.GA
        elif cmd.lower().strip() in ("4",f"{Faculty.CS.value.lower()}", "cs"):
            return Faculty.CS
        else:
            _C._inval(f"Enter '{cmd}' invalide")
            print(StudentPresenter._facultyToCliOPtion())


def _chooseGade() -> Grade:
    print(StudentPresenter._gradeToCliOption())
    while True:
        cmd = input(f"{_C.BOLD}> {_C.RESET}").strip().lower()
        if cmd.lower().strip() in ("1", f"{Grade.PREP.value.lower()}"):
            return Grade.PREP
        elif cmd.lower().strip() in ("2", f"{Grade.FRESHMAN.value.lower()}"):
            return Grade.FRESHMAN
        elif cmd.lower().strip() in ("3", f"{Grade.SOFOMORE.value.lower()}"):
            return Grade.SOFOMORE
        elif cmd.lower().strip() in ("4", f"{Grade.JUNIOR.value.lower()}"):
            return Grade.JUNIOR
        elif cmd.lower().strip() in ("5", f"{Grade.SENIOR.value.lower()}"):
            return Grade.SENIOR
        else:
            _C._inval(f"Enter '{cmd}' Invalide")
            print(StudentPresenter._gradeToCliOption())



def runCliApp() -> None:
    repository = InMemoryRepository(REPOSITORY_FILE)
    controller = StudentController(repository)

    _C._banner("Clean Architecture Student Manager CLI")

    while True:
        print(f"{COMMANDS}\n")
        try:
            cmd = input(f"{_C.BOLD}> {_C.RESET}").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{_C.BOLD}    Bye!{_C.RESET}\n")
            break

        if cmd in ("quit", "exit", "q", "0"):
            print(f"\n{_C.BOLD}    Bye!{_C.RESET}\n")
            break

        elif cmd in ("add", "1"):
            id = int(input("ID          : "))
            firstname = input("Firstname   : ")
            lastname = input("Lastname    : ")
            faculty = _chooseFaculty() 
            grade = _chooseGade()
            gpa = float(input("GPA         : "))
            output = controller.addStudent(id, firstname, lastname, faculty, grade, gpa)
            print(f"\nSucces: {output["succes"]}\n")
            if not output["succes"]:
                _C._err(f"{output["message"]}\n")
            else:
                print(StudentPresenter._toCliDetail(output["student"]))
                _C._ok(f"{output["message"]}\n")


        elif cmd in ("list", "2"):
            output = controller.showStudent(None, None)
            print(StudentPresenter._toCliRow(output["students"]))

        elif cmd in ("search by id", "3"):
            id = int(input("ID          : "))
            output = controller.searchStudentById(id)
            print(f"\nSucces: {output["succes"]}\n")
            if not output["succes"]:
                _C._err(f"{output["message"]}\n")
            else:
                print(StudentPresenter._toCliDetail(output["student"]))
                _C._ok(f"{output["message"]}\n")

        elif cmd in ("search by name", "4"):
            firstname = input("Firstname   : ")
            lastname = input("Lastname    : ")
            output = controller.searchStudentByName(firstname, lastname)
            print(f"\nSucces: {output["succes"]}\n")
            if not output["succes"]:
                _C._err(f"{output["message"]}\n")
            else:
                print(StudentPresenter._toCliDetail(output["student"]))
                _C._ok(f"{output["message"]}\n")
            
        elif cmd in ("delete", "5"):
            while True:
                try:
                    id = int(input("ID          : "))
                    break
                except ValueError as e:
                    print("ID invalide")
            output = controller.deleteStudent(id)
            print(f"\nSucces: {output["succes"]}\n")
            if not output["succes"]:
                _C._err(f"{output["message"]}\n")
            else:
                _C._ok(f"{output["message"]}\n")      

        else:
            _C._inval(f"Enter '{cmd}' invalide")