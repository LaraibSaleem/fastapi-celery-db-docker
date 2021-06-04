from .models.user_model import User
#from .celery.tasks import save_data
from .celery.worker import celery
from .database import SessionLocal, engine
import json


def user_exists(id) -> bool:
    db=SessionLocal()
    db_user = db.query(User).filter(User.id == id).first()
    db.close()
    if db_user:
        return True
    else:
        return False


def add_user(user):
    print("**********THIS IS USER OF CRUD************", user)
    tname = "save_data"

    # user.name = str(user.name)
    # user.friends = str(user.friends)

    # use delay() method to call the celery task
    # using send_task instead of delay to have task id in result

    '''
    celery.send_task(tname, args=(user.id, user.index, user.guid, user.isActive, user.balance,
                                 user.picture, user.age, user.eyeColor,
                                 # user.name,
                                 user.company, user.email, user.phone, user.address, user.about, user.latitude,
                                 user.longitude, user.tags, user.range,
                                 # user.friends,
                                 user.greeting, user.favoriteFruit))
    '''
    print("**********THIS IS DATA TYPES OF USER OF CRUD************")
    print("user.id", type(user.id))
    print("user.index", type(user.index))
    print("user.guid", type(user.guid))
    print("user.isActive", type(user.isActive))
    print("user.balance", type(user.balance))
    print("user.balance", type(user.balance))
    print("user.picture", type(user.picture))
    print("user.age", type(user.age))
    print("user.eyeColor", type(user.eyeColor))
    print("user.name", type(user.name))
    print("user.company", type(user.company))
    print("user.email", type(user.email))
    print("user.phone", type(user.phone))
    print("user.address", type(user.address))
    print("user.about,", type(user.about))
    print("user.latitude", type(user.latitude))
    print("user.longitude", type(user.longitude))
    print("user.tags", type(user.tags))
    print("user.range", type(user.range))
    print("user.friends", type(user.friends))
    print("user.greeting", type(user.greeting))
    print("user.favoriteFruit", type(user.favoriteFruit))



    celery.send_task(tname, args=("HELLO CRUD!", user.id, user.index, user.guid, user.isActive, user.balance,
                                 user.picture, user.age, user.eyeColor,
                                 #user.name,
                                 user.company, user.email, user.phone, user.address, user.about, user.latitude, user.longitude,
                                 user.tags,
                                 user.range,
                                 #user.friends,
                                 user.greeting, user.favoriteFruit))
    #args have an extra argument as "HELLO CRUD!" bcz tasks.py celery task was ignoring 1st