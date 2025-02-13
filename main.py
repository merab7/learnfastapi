from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hellow world"}


@app.get("/users/{user_name}")
async def read_user(user_name: str):
    return {"user_name": user_name}


@app.get("/users/user_id/{user_id}")
async def get_id(user_id: int):
    return {"user_id": user_id}
