from dataclasses import dataclass
from src.entities.student_entitie import Student, Grade, Faculty, InvalideData
from src.use_case.interface.interface import StudentRepo
from typing import Optional


@dataclass
class UpdateStudentInput:
    id : str
    photo : str
    faculty : Optional[Faculty] = None
    grade : Optional[Grade] = None
    gpa : Optional[str] = None


@dataclass
class UpdateStudentOuput:
    message : str
    status : bool
    student : Optional[Student] = None


class UpdateStudent:
    def __init__(self, repository:StudentRepo) -> None:
        self.repository = repository

    def execute(self, input_data:UpdateStudentInput) -> UpdateStudentOuput:
        student = self.repository.getStudentByID(input_data.id)
        if not student:
            return UpdateStudentOuput(
                message = f"No student with ID:{input_data.id} has been found",
                status = False,
                student = None
            )

        PHOTO_M = ""
        FACULTY_M = ""
        GRADE_M = ""
        GPA_M = ""

        if input_data.photo:
            student.photo = input_data.photo
            PHOTO_M = f"Photo has been updated successfully"

        if input_data.faculty:
            if student._in_prep():
                student.faculty = input_data.faculty
                FACULTY_M = f"\nFaculty has been updated to {input_data.faculty.value} successfully"
            else:
                FACULTY_M = f"\nCannot change Faculty after {Grade.PREP.value}"

        if input_data.grade:
            if student.validateGrade(input_data.grade):
                student.grade = input_data.grade
                GRADE_M = f"\nGrade has been updated to {input_data.grade.value} successfully"
            else: 
                GRADE_M = f"\nStudent with ID:{input_data.id} cannot raise in {input_data.grade.value}"

        if input_data.gpa:
            student.gpa = input_data.gpa
            GPA_M = f"\nGPA has been updated to {input_data.gpa} successfully"

        try:
            checked_student = Student(id=student.id, firstname=student.firstname, lastname=student.lastname, photo=student.photo, faculty=student.faculty, grade=student.grade, gpa=student.gpa)
        except InvalideData as e:
            return UpdateStudentOuput(message = f"{e}", status = False, student = None)
            
        updated_student = self.repository.updateStudent(checked_student)

        return UpdateStudentOuput(
            message = f"{PHOTO_M} {FACULTY_M} {GRADE_M} {GPA_M}",
            status = True,
            student = updated_student,
        )

        