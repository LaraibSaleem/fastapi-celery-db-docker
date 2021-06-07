from celery.utils.log import get_task_logger
#from starlette.responses import JSONResponse
import logging
from backend.database import SessionLocal, engine
from backend.models.user_model import User, Friends
from backend.models import user_model
from .worker import celery
from datetime import datetime


user_model.Base.metadata.create_all(bind=engine)


LOGGER = logging.getLogger(__name__)
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)



# Add User to Database - Run Asynchronously with celery
# Example process of long running task
@celery.task(name="save_user", serializer='json')
def save_user(self, *user):
    print("**********THIS IS USER OF TASK************", user)

    try:

        '''
        for i in user:
            print(f"{i}\n\t*****************_____________________ {type(user[i])}_______****************")
        '''

        date = datetime.now()
        #print("**********DATE************", date)
        name = {"first": user[8], "last": user[9]}

        db_user = User(id=user[0], index=user[1], guid=user[2], isActive=user[3], balance=user[4],
                       picture=user[5], age=user[6], eyeColor=user[7],
                        name=name,
                        company=user[10], email=user[11], phone=user[12], address=user[13], about=user[14], registered=date, latitude=user[15], longitude=user[16],
                        tags=user[17],
                        range=user[18],
                        #friends=user[18]
                        greeting=user[19], favoriteFruit=user[20])
        db = SessionLocal()
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    except Exception as ex:
        print(f"\n\t_____*****_____{ex}_____*****_____\n\t")
        raise ex
    #return JSONResponse(status_code=200, content={"message": "User record has been added."})
    return {"msg": "Hello Save User!"}



@celery.task(name="save_frnds", serializer='json')
def save_frnds(self, u_id, *frnd):
    try:
        print("**********THIS IS FRIENDS and ID of USER OF TASK************", frnd, u_id)

        db_frnd = Friends(id=frnd[0], name=frnd[1], user_id=u_id)
        db = SessionLocal()
        db.add(db_frnd)
        db.commit()
        db.refresh(db_frnd)
    except Exception as ex:
        print(f"\n\t_____*****_____{ex}_____*****_____\n\t")
        raise ex

    return {"msg": "Hello Save Friends!"}