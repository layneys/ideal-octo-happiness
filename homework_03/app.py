from fastapi import FastAPI

app = FastAPI()


@app.get("/ping/")
def ping_pong():
    return {"message": "pong"}

