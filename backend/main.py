from fastapi import FastAPI
klu = FastAPI(title="AI Tutor",
              description="AI Tutor PBL Project",
              version="1.0.0")
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