from fastapi import Depends, FastAPI, HTTPException
from backend import crud
from backend.schemas.user_schema import User
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
#from backend.database import SessionLocal, engine
from typing import List


# user_model.Base.metadata.create_all(bind=engine)

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