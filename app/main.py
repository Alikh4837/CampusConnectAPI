from fastapi import FastAPI

app = FastAPI(title="University course registration and resource management API")

@app.get("/")
def root():
    return {"Message":"Api is currently running"}