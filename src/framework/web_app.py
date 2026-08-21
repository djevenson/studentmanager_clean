import os
import uuid
from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.interface_adapter.presenters.presenter import StudentPresenter
from src.interface_adapter.repositories.sql_repo import SqlStudentIdGenerator, PosGreSQLSudentRepot
from src.interface_adapter.repositories.sql_connection import build_db_connection_string
from src.interface_adapter.repositories.memory_repo import InMemoryRepository, InMemoryStudentIdGenerator
from src.interface_adapter.controller.controller import StudentController
from src.entities.student_entitie import Faculty, Grade



UPLOAD_DIR = "UPLOADS"
os.makedirs(UPLOAD_DIR,exist_ok=True)

REPOSITORY_FILE = "src/interface_adapter/repositories/student_repo.json"
MEMORY_REPO = InMemoryRepository(REPOSITORY_FILE)
MEMORY_ID = InMemoryStudentIdGenerator(MEMORY_REPO)

SQL_REPO = PosGreSQLSudentRepot(build_db_connection_string())
SQL_ID = SqlStudentIdGenerator(SQL_REPO)


"""class AddStudent(BaseModel):
    firstname : str
    lastname : str
    photo : UploadFile = File
    faculty : Faculty = Query"""


def createAPP():
    app = FastAPI(
        title = "STUDENT MANAGER API",
        description = "REST API FOR A STUDENT MANAGER THAT CAN ADD AND UPDATE SUDENT",
        version = "1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )

    controller = StudentController(SQL_REPO, SQL_ID)
    presenter = StudentPresenter()


    @app.get("/health")
    async def health_check():
        return {"status": "great"}


    @app.post("/students")
    async def add_student(firstname : str, lastname : str, photo : UploadFile = File, faculty : Faculty = Query(Faculty.CE)):
        ext = photo.filename.rsplit(".",1)[-1]
        photo_name = f"{lastname}_{uuid.uuid4()}.{ext}"
        photo_url = (os.path.join(UPLOAD_DIR, photo_name)).replace("\\","/")

        result = controller.addStudent(firstname, lastname, faculty, photo_url)

        if not result["succes"]:
            raise HTTPException( status_code= 201, detail= result["message"])

        with open (photo_url,"wb")as f:
            f.write(await photo.read())
        
        return {
            "message": result["message"], 
            "student": presenter._toDict(result["student"])
        }
        

    @app.get("/students/{id}")
    async def get_by_id(id:str):
        result = controller.searchStudentById(id)
        if not result["succes"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return {
            "message": result["message"], 
            "student": presenter._toDict(result["student"])
        }


    @app.get("/students/{firstname}{lastname}")
    async def get_by_name(firstname:str, lastname:str):
        result = controller.searchStudentByName(firstname, lastname)
        if not result["succes"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return {
            "message": result["message"], 
            "student": presenter._toDict(result["student"])
        }


    @app.get("/student")
    async def get_student(faculty:Faculty=Query(None), grade:Grade=Query(None)):
        result = controller.showStudent(faculty, grade)
        return {
            "faculty": result["faculty"], 
            "grade": result["grade"], 
            "students": presenter._toListDisct(result["students"]), 
            "total": result["total"]
        }


    @app.delete("/students/delete/{id}")
    async def delete_student(id:str):
        result = controller.deleteStudent(id)
        if not result["succes"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return {
            "message": result["message"], 
        }

    app.mount("/UPLOADS",StaticFiles(directory="UPLOADS"),name="UPLOADS")

    return app