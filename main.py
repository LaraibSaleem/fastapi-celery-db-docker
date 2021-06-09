from fastapi import Depends, FastAPI, HTTPException
from fastapi.logger import logger as fastapi_logger
from backend import crud
from backend.schemas.user_schema import User, Friends
from starlette.responses import RedirectResponse
from typing import List
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


# Home/welcome route
@app.get("/", tags=["Root"])
def read_root():
    return RedirectResponse(url="/docs/")
    #return {"greeting":"Hello World!"}


@app.post("/users/", response_model=List[User], tags=["User"])
def add_user(user: User):
    """User Post API"""

    if crud.user_exists(user.id):
        raise HTTPException(status_code=400, detail="ID already exists.")
    else:
        crud.add_user(user)
    return [user]



@app.post("/users/{id}/friends/", response_model=Friends, tags=["User Friends"])
def add_user_frnd(frnd: Friends, id: str):
    """Friends Post API"""

    #crud.add_user_frnd(frnd, id)
    return crud.add_user_frnd(frnd, id) #not really a celery task, will have to wait a little bit - as there was error (of missing values) when [frnd, id] was returned.
    #return [frnd, id]