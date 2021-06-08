from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict


class Name(BaseModel):
    first: str
    last: str

    class Config:
        orm_mode = True


class Friends(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# user schema to store users
class User(BaseModel):
    id: str = Field(..., max_length=25, min_length=20)
    index: int = Field(...)
    guid: str = Field(...)
    isActive: bool = Field(...)
    balance: str = Field(...)
    picture: str = Field(...)                                  #"http://placehold.it/32x32"
    age: int = Field(...)
    eyeColor: str = Field(...)
    name: Name  #= Field(...)                                  #{"first": "Kent",last": "Barnes"}
    company: str = Field(...)
    email: EmailStr = Field(...)
    phone: str = Field(...)                                    #"+1 (997) 579-4000"
    address: str = Field(...)
    about: str = Field(...)
    #registered: "Wednesday, November 30, 2016 1:58 PM"
    latitude: float = Field(..., ge=-90, le=90)                                #"79.553559"
    longitude: float = Field(..., ge=-180, le=180)                               #"-109.466046"
    tags: List[str] = [] # = Field(...)                         #["voluptate","non","nulla","id", "esse"]
    range: List[int] = [0,1,2,3,4,5,6,7,8,9] # = Field(...)     #[0,1,2,3,4,5,6,7,8,9]
    friends: List[Friends] # = Field(...)
    ''' [{"id": 0,"name": "Chrystal Harris"},
    {"id": 1,"name": "Lula Delgado"},
    {"id": 2,"name": "Galloway Perkins"}] '''
    greeting: str = Field(...)
    favoriteFruit: str = Field(...)

    class Config:
        orm_mode = True