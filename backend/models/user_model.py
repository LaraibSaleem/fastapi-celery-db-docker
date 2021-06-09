from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


# user model to store users
class User(Base):
    """User model/table of database"""

    __tablename__ = "User"

    id = Column(String(255), primary_key=True, index=True)
    index = Column(Integer, unique=True, autoincrement=True, index=True)
    guid = Column(String(255))
    isActive = Column(Boolean)
    balance = Column(String(255))
    picture = Column(String(255)) #"http://placehold.it/32x32"
    age = Column(Integer)
    eyeColor = Column(String(255))
    name = Column(JSON)  #{"first": "Kent",last": "Barnes"},
    company = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255)) #"+1 (997) 579-4000",
    address = Column(String(255))
    about = Column(String(255))
    registered = Column(DateTime) #"Wednesday, November 30, 2016 1:58 PM",
    latitude = Column(Float)      #"79.553559",
    longitude = Column(Float)      #"-109.466046",
    tags = Column(JSON)   #["voluptate","non","nulla","id", "esse"],
    range = Column(JSON)    #[0,1,2,3,4,5,6,7,8,9],
    greeting = Column(String(255))
    favoriteFruit = Column(String(255))

    friends = relationship("Friends", back_populates="user")


# friends model to store users' friends
class Friends(Base):
    """Friends model/table of database"""

    __tablename__ = "Friends"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255))
    user_id = Column(String(255), ForeignKey("User.id"))

    user = relationship("User", back_populates="friends")