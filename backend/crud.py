from .models.user_model import User
#from .celery.tasks import save_data
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
    name = "save_data"
    # use delay() method to call the celery task
    '''
    celery.send_task(name, args=None, kwargs={'id': user.id,
                                   'index' : user.index,
                                   'guid' : user.guid,
                                   'balance' : user.balance,
                                   'age' : user.age,
                                   'eyeColor' : user.eyeColor,
                                    'company' : user.company,
                                   'address' : user.address,
                                   'about' : user.about,
                                   'greeting' : user.greeting,
                                   'favoriteFruit' : user.favoriteFruit})
    '''
    celery.send_task(name, args=("HELLO CRUD.", user.id, user.index, user.guid, user.balance, user.age, user.eyeColor, user.company,
                                  user.address, user.about,  user.greeting,  user.favoriteFruit))
