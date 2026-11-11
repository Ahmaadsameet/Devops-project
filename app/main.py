from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "DevOps Demo API"}


@app.get("/health")
def health():
    return {"status": "healthy"}
