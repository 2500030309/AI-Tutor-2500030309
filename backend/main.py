from fastapi import FastAPI
import uvicorn

klu = FastAPI(title="AI Tutor")

@klu.get("/")
def home():
    return {"message" : "Welcome to AI Tutor Project..!"}

@klu.get("/demo")
def demo():
    return {"message" : "Korey wa KL University des !"}

@klu.get("/ask")
def ask():
    return {"message" : "What is meant by LLM?", 
            "answer":"LLM is meant by Large Language model"}

@klu.get("/student")
def student():
    return {"id":1,
            "name":"Rammm",
            "Gender":"Male",
            "course":"DSA"}

@klu.get("/students")
def getstudents():
    return [{"id":1,
            "name":"Rammm",
            "Gender":"Male",
            "course":"DSA"},
            {"id":2,
            "name":"Surya",
            "Gender":"Male",
            "course":"DSA"}]


if __name__ == "__main__":
    uvicorn.run("main:klu",host = "127.0.0.1",port = 2027, reload = True)