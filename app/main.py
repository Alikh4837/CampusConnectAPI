from fastapi import FastAPI
from app.routers.student import router as student_router

app = FastAPI(title="University course registration and resource management API")
# add_pagination(app)
app.include_router(student_router)


@app.get("/")
def root():
    return {"Message": "Api is currently running"}
