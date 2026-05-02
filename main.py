from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()
FILE_PATH = "courses.json"

class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str

def read_courses():
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_courses(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.get("/courses")
def get_courses():
    return read_courses()

@app.post("/courses")
def add_course(course: Course):
    courses = read_courses()
    new_course = course.model_dump()
    courses.append(new_course)
    write_courses(courses)
    
    return {"message": "과목이 성공적으로 추가되었습니다.", "data": new_course}