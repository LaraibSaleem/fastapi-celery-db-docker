from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, PickleType
from ..database import Base


# user model to store users
class User(Base):
    __tablename__ = "User"

    id = Column(String(255), primary_key=True, index=True)
    index = Column(Integer, autoincrement=True, index=True,  nullable=True)
    guid = Column(String(255),  nullable=True)
    isActive = Boolean
    balance = Column(String(255),  nullable=True)
    picture = Column(String(255),  nullable=True) #"http://placehold.it/32x32"
    age = Column(Integer,  nullable=True)
    eyeColor = Column(String(255),  nullable=True)
    #name = Column(JSON, nullable=True)  #{"first": "Kent",last": "Barnes"},
    company = Column(String(255),  nullable=True)
    email = Column(String(255),  nullable=True)
    phone = Column(String(255), nullable=True) #"+1 (997) 579-4000",
    address = Column(String(255),  nullable=True)
    about = Column(String(255), nullable=True)
    registered = Column(DateTime, nullable=True) #"Wednesday, November 30, 2016 1:58 PM",
    latitude = Column(Float, nullable=True)      #"79.553559",
    longitude = Column(Float, nullable=True)      #"-109.466046",
    tags = Column(JSON, nullable=True)    #["voluptate","non","nulla","id", "esse"],
    range = Column(JSON, nullable=True)    #[0,1,2,3,4,5,6,7,8,9],
    #friends= Column(PickleType(JSON))
    '''
    [{"id": 0, "name": "Chrystal Harris"},
     {"id": 1, "name": "Lula Delgado"},
     {"id": 2, "name": "Galloway Perkins"}]
    '''
    greeting = Column(String(255))
    favoriteFruit = Column(String(255))
