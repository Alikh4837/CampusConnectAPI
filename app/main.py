from fastapi import FastAPI
from fastapi_pagination import Page,add_pagination,paginate

app = FastAPI(title="University course registration and resource management API")
# add_pagination(app)

@app.get("/")
def root():
    return {"Message":"Api is currently running"}