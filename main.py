from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return "This is the home page"