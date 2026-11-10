from fastapi import FastAPI
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