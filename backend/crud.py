from .models.user_model import User, Friends
from .celery.tasks import save_user, save_frnds
from .celery.worker import celery
from .database import SessionLocal, engine


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
    tname = "save_user"

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

    celery.send_task(tname, args=("HELLO ADD USER!", user.id, user.index, user.guid, user.isActive, user.balance,
                                 user.picture, user.age, user.eyeColor,
                                 user.name.first,
                                 user.name.last,
                                 user.company, user.email, user.phone, user.address, user.about, user.latitude, user.longitude,
                                 user.tags,
                                 user.range,
                                 #user.frnds
                                 user.greeting, user.favoriteFruit))
    #args have an extra argument as "HELLO CRUD!" bcz tasks.py celery task was ignoring 1st



def add_user_frnd(frnd, u_id):
    print("**********THIS IS FRIENDS and ID of USER OF CRUD************", frnd, u_id)

    tname = "save_frnds"
    celery.send_task(tname, args=("HELLO ADD USER ITEM", u_id, frnd.id, frnd.name))
    #celery.send_task(tname, args=(u_id, frnd.id, frnd.name))