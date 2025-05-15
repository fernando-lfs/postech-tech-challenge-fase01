from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API funcionando"}


# uvicorn app.main:app --reload
