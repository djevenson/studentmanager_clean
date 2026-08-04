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