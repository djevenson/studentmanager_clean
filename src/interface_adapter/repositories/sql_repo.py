import psycopg2
from src.entities.student_entitie import ID_SIZE, Student, Faculty, Grade
from typing import Optional
from src.use_case.interface.interface import StudentRepo, StudentIdGeneratorInterface
from datetime import datetime



class PosGreSQLSudentRepot:
    def __init__(self, db_info):
        self.db_info = db_info
        self._init_shema()

    def _init_shema(self):
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""   
                    CREATE TABLE IF NOT EXISTS students (
                    id          VARCHAR(10) PRIMARY KEY,
                    firstname   VARCHAR(120) NOT NULL,
                    lastname    VARCHAR(120) NOT NULL,
                    photo       VARCHAR(120),
                    faculty     VARCHAR(5),
                    grade       VARCHAR(10),
                    gpa         VARCHAR(4)
                    )
                """)

    def addStudent(self, student:Student) -> Optional[Student]:
         with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO students (id, firstname, lastname, photo, faculty, grade, gpa)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, self._toRow(student),)
                return student

    def deleteStudent(self, id:str) -> bool:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM students WHERE id = %s
                """, (id,))
                return cursor.rowcount > 0

    def getStudentByID(self, id:str) -> Optional[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM students WHERE id = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    return self._fromRow(row)
                return None

    def getStudentByName(self, firstname:str, lastname:str) -> Optional[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM students WHERE firstname = %s AND lastname = %s
                """, (firstname, lastname))
                row = cursor.fetchone()
                if row:
                    return self._fromRow(row)
                return None

    def getAllStudent(self) -> list[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
                return [self._fromRow(row) for row in rows]

    def getAllStudentByFaculty(self, faculty:Faculty) -> list[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM students WHERE faculty = %s
                """, (faculty.name,))
                rows = cursor.fetchall()
                return [self._fromRow(row) for row in rows]

    def getAllStudentByGrade(self, grade:Grade) -> list[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM students WHERE grade = %s
                """, (grade.name,))
                rows = cursor.fetchall()
                return [self._fromRow(row) for row in rows]

    def getAllStudentByFacultyGrade(self, faculty:Faculty, grade:Grade) -> list[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM students WHERE faculty = %s AND grade = %s
                """, (faculty.name, grade.name))
                rows = cursor.fetchall()
                return [self._fromRow(row) for row in rows]

    def updateStudent(self, student:Student) -> Optional[Student]:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE students SET photo=%s, faculty=%s, grade=%s, gpa=%s WHERE id=%s RETURNING *
                """, (student.photo, student.faculty.name, student.grade.name, student.gpa, student.id))
                rows = cursor.fetchall()
                return [self._fromRow(row) for row in rows]

    def getLastRank(self, prefix:str) -> int:
        with self._getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id FROM students WHERE id LIKE %s
                """, (prefix + '%',))
                rows = cursor.fetchall()
                matching_ranks = [int(row[0][6:]) for row in rows if len(row[0]) == ID_SIZE]
                return max(matching_ranks, default=0)

    def _getConnection(self): # -> connection
        connetion = psycopg2.connect(self.db_info)
        return connetion

    def _toRow(self, student:Student) -> tuple:
        return (
            student.id, student.firstname, student.lastname, student.photo,
            student.faculty.name, student.grade.name, student.gpa
        )
    def _fromRow(self, row:tuple) -> Student:
        return Student(
            id=row[0],
            firstname=row[1],
            lastname=row[2],
            photo=row[3],
            faculty=Faculty[row[4]],
            grade=Grade[row[5]],
            gpa=row[6]
        )

class SqlStudentIdGenerator(StudentIdGeneratorInterface):
    _FACULTY_CODE = {"CE":1, "BA":2, "GA":3, "CS":4}

    def __init__(self, repository: StudentRepo) -> None:
        self._repository = repository

    def generate(self, faculty:Faculty) -> str:
        prefix = f"{datetime.now().year}{self._FACULTY_CODE[faculty.name]:02d}"  
        rank = self._repository.getLastRank(prefix) + 1
        id = f"{prefix}{rank:04d}"
        return id