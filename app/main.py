from fastapi import FastAPI
from app.database import create_tables
from app.routes import tasks

app = FastAPI(
    title="Task Management API",
    description="A simple RESTful API to manage tasks",
    version="1.0.0"
)

# Create tables on startup
@app.on_event("startup")
def startup():
    create_tables()

# Register routes
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to the Task Management API!"}
