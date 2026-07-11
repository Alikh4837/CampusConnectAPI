from fastapi import FastAPI
from app.routers.student import router as student_router
from app.routers.instructor import router as instructor_router
from app.routers.department import router as department_router
from app.routers.room import router as room_router
from app.routers.term import router as term_router
from app.routers.course import router as course_router
from app.routers.section import router as section_router
from app.routers.enrollment import router as enrollment_router

app = FastAPI(title="University course registration and resource management API")
# add_pagination(app)
app.include_router(student_router)
app.include_router(instructor_router)
app.include_router(department_router)
app.include_router(room_router)
app.include_router(term_router)
app.include_router(course_router)
app.include_router(section_router)
app.include_router(enrollment_router)


@app.get("/")
def root():
    return {"Message": "Api is currently running"}
