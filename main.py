from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the Drawing Works backend database API"

@app.get("/test")
def read_test():
    return "This is a test endpoint!"
