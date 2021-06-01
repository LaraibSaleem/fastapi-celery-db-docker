from pydantic import BaseModel, EmailStr
from typing import List, Dict


# user schema to store users
class User(BaseModel):
    id: str
    index: int
    guid: str
    #isActive: bool,
    balance: str
    #picture: "http://placehold.it/32x32"
    age: int
    eyeColor: str
    #name: Dict{"first": str, "last": str}   #{"first": "Kent",last": "Barnes"},
    company: str
    #email: EmailStr
    #phone: "+1 (997) 579-4000",
    address: str
    about: str
    #registered: "Wednesday, November 30, 2016 1:58 PM",
    #latitude: float      #"79.553559",
    #longitude: float     #"-109.466046",
    #tags: List    #["voluptate","non","nulla","id", "esse"],
    #range: List   #[0,1,2,3,4,5,6,7,8,9],
    #friends: List
    ''' [{"id": 0,"name": "Chrystal Harris"},
    {"id": 1,"name": "Lula Delgado"},
    {"id": 2,"name": "Galloway Perkins"}] '''
    greeting: str
    favoriteFruit: str

    class Config:
        orm_mode = True