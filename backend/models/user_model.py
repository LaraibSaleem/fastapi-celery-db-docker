from sqlalchemy import Column, Integer, String, Float
from ..database import Base


# user model to store users
class User(Base):
    __tablename__ = "User"

    id = Column(String(255), primary_key=True, index=True)
    index = Column(Integer, autoincrement=True, index=True)
    guid = Column(String(255))
    # isActive = bool,
    balance = Column(String(255))
    # picture = "http://placehold.it/32x32"
    age = Column(Integer)
    eyeColor = Column(String(255))
    # name = JSON{"first": str, "last": str}   #{"first": "Kent",last": "Barnes"},
    company = Column(String(255))
    # email = EmailStr
    # phone = "+1 (997) 579-4000",
    address = Column(String(255))
    about = Column(String(255))
    #registered= "Wednesday, November 30, 2016 1:58 PM",
    # latitude= Column(Float)      #"79.553559",
    # longitude= Column(Float)      #"-109.466046",
    # tags= List    #["voluptate","non","nulla","id", "esse"],
    # range= List   #[0,1,2,3,4,5,6,7,8,9],
    # friends= List
    '''
    [{"id": 0, "name": "Chrystal Harris"},
     {"id": 1, "name": "Lula Delgado"},
     {"id": 2, "name": "Galloway Perkins"}]
    '''
    greeting = Column(String(255))
    favoriteFruit = Column(String(255))