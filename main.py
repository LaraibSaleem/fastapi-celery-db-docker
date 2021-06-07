from fastapi import Depends, FastAPI, HTTPException
from backend import crud
from backend.schemas.user_schema import User, Friends
from starlette.responses import RedirectResponse
from typing import List


app = FastAPI()

# Home/welcome route
@app.get("/", tags=["Root"])
def read_root():
    return RedirectResponse(url="/docs/")
    #return {"greeting":"Hello World!"}


@app.post("/users/", response_model=List[User], tags=["User"])
def add_user(user: User):
    print("**********THIS IS USER OF MAIN************", user)

    if crud.user_exists(user.id):
        raise HTTPException(status_code=400, detail="ID already exists.")
    else:

        crud.add_user(user)
    return [user]


@app.post("/users/{id}/friends/", response_model=Friends, tags=["User Friends"])
def add_user_frnd(frnd: Friends, id: str):
    #crud.add_user_frnd(frnd, id)
    return crud.add_user_frnd(frnd, id)
    #return [frnd, id]